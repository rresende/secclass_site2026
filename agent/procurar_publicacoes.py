"""
Agente quinzenal: procura trabalhos novos que usem ou refiram o SECClasS e
acrescenta-os a src/data/publicacoes.yml com estado "proposta".

Fluxo
  1. Pesquisa (Claude + ferramenta web_search do servidor) em repositórios
     universitários portugueses (RCAAP e repositórios institucionais),
     atas de congressos de BIM (PTBIM, etc.) e bases bibliográficas.
  2. Extração estruturada (saída JSON validada) dos campos de cada trabalho.
  3. Remoção de duplicados face ao ficheiro existente.
  4. Escrita das propostas; o workflow abre um pull request para revisão.

Nada é publicado sem aprovação humana: as entradas novas ficam com
estado "proposta" e só aparecem no site quando passarem a "publicado".

Requer: ANTHROPIC_API_KEY (segredo do repositório no GitHub).
"""

from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys
import unicodedata
from typing import List, Literal, Optional

import anthropic
import yaml
from pydantic import BaseModel, Field

MODEL = "claude-opus-5-5"
DATA = pathlib.Path(__file__).resolve().parents[1] / "src" / "data" / "publicacoes.yml"

DOMINIOS = [
    # Agregador nacional e universidades/politécnicos (inclui todos os subdomínios,
    # p.ex. repositorium.sdum.uminho.pt e as atas PTBIM da UMinho Editora)
    "rcaap.pt", "iscte-iul.pt", "uminho.pt", "up.pt", "ulisboa.pt", "unl.pt",
    "uc.pt", "ua.pt", "uevora.pt", "ualg.pt", "ubi.pt", "utad.pt", "uac.pt",
    "ipp.pt", "ipl.pt", "ipb.pt", "ipleiria.pt", "ipcb.pt", "ipv.pt", "lnec.pt",
    # Congressos de BIM e bases bibliográficas
    "ptbim.org", "researchgate.net", "mdpi.com", "sciencedirect.com",
    "openalex.org", "crossref.org", "doi.org", "scholar.archive.org", "zenodo.org",
]


class Trabalho(BaseModel):
    titulo: str
    autores: List[str]
    instituicao: str = Field(description="Instituição(ões) dos autores ou onde o trabalho foi apresentado/defendido")
    local: str = Field(description="Revista, congresso, ou repositório e tipo de grau")
    ano: int
    tipo: Literal["artigo", "comunicacao", "dissertacao", "tese", "relatorio", "livro"]
    resumo: str = Field(description="Resumo em português europeu, 2 a 4 frases, fiel ao original")
    papel_secclass: str = Field(description="Como o trabalho usa ou refere o SECClasS, numa frase concreta")
    url: str = Field(description="Link direto para o trabalho (página do repositório, DOI ou PDF)")
    evidencia: str = Field(description="Excerto curto do texto do trabalho onde o SECClasS é mencionado")
    confianca: Literal["alta", "media", "baixa"]


class Resultado(BaseModel):
    trabalhos: List[Trabalho]


def normalizar(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def carregar() -> list[dict]:
    return yaml.safe_load(DATA.read_text(encoding="utf-8")) or []


def pesquisar(client: anthropic.Anthropic, conhecidos: list[str]) -> str:
    """Passo 1: pesquisa web livre, devolve notas de investigação em texto."""
    hoje = dt.date.today().isoformat()
    prompt = f"""Hoje é {hoje}. Procura trabalhos académicos e técnicos (artigos, comunicações em congressos,
dissertações de mestrado, teses, relatórios) que usem, apliquem, avaliem ou refiram explicitamente o
SECClasS — o sistema de classificação da construção português adaptado do Uniclass 2015
(também escrito "SECClass", "Sustainability Enhanced Construction Classification System").

Onde procurar, por esta ordem:
1. RCAAP (rcaap.pt) e repositórios institucionais das universidades e politécnicos portugueses.
2. Atas dos congressos portugueses de BIM (PTBIM) e de outros congressos de construção.
3. Revistas e bases bibliográficas (MDPI, ScienceDirect, OpenAlex, Crossref, ResearchGate).

Pesquisa em português e em inglês. Abre a página de cada candidato para confirmar que o SECClasS é
mesmo mencionado no texto (não basta falar de "sistemas de classificação" ou de Uniclass).

Estes trabalhos já estão registados; ignora-os:
{chr(10).join('- ' + t for t in conhecidos)}

Para cada trabalho novo confirmado, regista: título exato, autores, instituição, local de publicação,
ano, tipo, um resumo fiel, de que forma usa o SECClasS, o URL direto e um excerto que prove a menção.
Se não encontrares nada novo, diz isso claramente. Não inventes trabalhos nem URLs."""

    messages = [{"role": "user", "content": prompt}]
    tools = [{"type": "web_search_20260209", "name": "web_search", "max_uses": 25,
              "allowed_domains": DOMINIOS}]
    partes: list[str] = []
    for _ in range(6):  # retoma turnos em pausa (pause_turn)
        with client.beta.messages.stream(
            model=MODEL,
            max_tokens=64000,
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            output_config={"effort": "high"},
            tools=tools,
            messages=messages,
        ) as stream:
            resp = stream.get_final_message()
        if resp.stop_reason == "refusal":
            sys.exit("Pedido recusado pelo modelo; sem propostas.")
        partes += [b.text for b in resp.content if b.type == "text"]
        if resp.stop_reason != "pause_turn":
            break
        messages.append({"role": "assistant", "content": resp.content})
    return "\n".join(partes)


def extrair(client: anthropic.Anthropic, notas: str) -> list[Trabalho]:
    """Passo 2: converte as notas em registos validados (sem ferramentas)."""
    resp = client.messages.parse(
        model=MODEL,
        max_tokens=16000,
        output_config={"effort": "medium"},
        messages=[{"role": "user", "content":
            "Converte as notas abaixo em registos estruturados. Inclui apenas trabalhos cuja menção ao "
            "SECClasS esteja confirmada nas notas, com URL presente nas notas. Escreve resumo e "
            "papel_secclass em português europeu. Se não houver trabalhos, devolve lista vazia.\n\n"
            f"<notas>\n{notas}\n</notas>"}],
        output_format=Resultado,
    )
    if resp.stop_reason == "refusal" or resp.parsed_output is None:
        return []
    return resp.parsed_output.trabalhos


def main() -> int:
    existentes = carregar()
    titulos = {normalizar(p.get("titulo", "")) for p in existentes}
    urls = {p.get("url") for p in existentes if p.get("url")}

    client = anthropic.Anthropic()
    notas = pesquisar(client, [p["titulo"] for p in existentes])
    novos = [t for t in extrair(client, notas)
             if t.confianca != "baixa"
             and normalizar(t.titulo) not in titulos
             and t.url not in urls]

    if not novos:
        print("Sem trabalhos novos.")
        return 0

    hoje = dt.date.today().isoformat()
    bloco = yaml.safe_dump(
        [{
            "titulo": t.titulo, "autores": t.autores, "instituicao": t.instituicao,
            "local": t.local, "ano": t.ano, "tipo": t.tipo, "categoria": "terceiros",
            "resumo": t.resumo, "papel_secclass": t.papel_secclass, "url": t.url, "ficheiro": "",
            "estado": "proposta", "fonte": f"agente ({t.confianca}) — evidência: {t.evidencia}",
            "adicionado": hoje,
        } for t in novos],
        allow_unicode=True, sort_keys=False, width=120,
    )
    with DATA.open("a", encoding="utf-8") as f:
        f.write(f"\n# --- Propostas do agente, {hoje}: rever e mudar estado para 'publicado' ---\n")
        f.write(bloco)
    print(f"{len(novos)} proposta(s) acrescentada(s).")
    for t in novos:
        print(f"- {t.titulo} ({t.ano}) {t.url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""
Gera scripts/dados/secclass.json (dados para uma pesquisa rápida no site) a partir do Excel das tabelas.

EM ESPERA: a pesquisa rápida no site não está ativa (a decidir com a equipa da app pesquisa.secclass.pt).
Para a ativar, o ficheiro gerado deve passar para public/data/ e ser lido por um script da página /pesquisa/.

Uso (ao publicar uma nova versão do SECClasS):
    pip install openpyxl
    python scripts/gerar_dados_pesquisa.py "Tabelas SECClasS V2.0.xlsx" 2.0

O Excel é o ficheiro publicado nas releases do repositório rresende/secclass.
"""
import json
import pathlib
import sys

import openpyxl

xlsx, versao = sys.argv[1], sys.argv[2]
ws = openpyxl.load_workbook(xlsx, read_only=True)["Todas_Tabelas"]
linhas = list(ws.iter_rows(values_only=True))
cab = [str(c).strip() if c else "" for c in linhas[0]]
i = {n: cab.index(n) for n in ("Tabela", "Codigo", "Titulo SECClasS", "Nível", "Titulo Uniclass")}

termos = []
for r in linhas[1:]:
    codigo = (r[i["Codigo"]] or "").strip()
    if not codigo:
        continue
    pt = (r[i["Titulo SECClasS"]] or "").strip()
    en = (r[i["Titulo Uniclass"]] or "").strip()
    nacional = en.lower().startswith("termo introduzido pelo secclass")
    termos.append([codigo, pt, "" if nacional else en, 1 if nacional else 0])

out = pathlib.Path(__file__).resolve().parent / "dados" / "secclass.json"
out.write_text(json.dumps({"versao": versao, "termos": termos}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"{len(termos)} termos -> {out} ({out.stat().st_size // 1024} KB)")

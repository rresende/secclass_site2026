# Site SECClasS (2026)

Site estático do **SECClasS — Sistema de Classificação da Construção Orientado para a Sustentabilidade**.
Mantido pela Escola de Tecnologias Digitais Aplicadas do Iscte Sintra, com contributos técnicos da comunidade.

- **Tecnologia:** [Astro](https://astro.build), gerado em HTML estático. Não há base de dados, PHP, plugins nem área de administração para atacar.
- **Publicação:** GitHub Pages, automaticamente a cada alteração no ramo `main` (`.github/workflows/deploy.yml`).
- **Dados das tabelas:** repositório [`rresende/secclass`](https://github.com/rresende/secclass) (releases).

## Como atualizar (sem programar)

Todo o conteúdo está em três ficheiros de texto. No GitHub, abra o ficheiro, carregue no lápis ✏️, edite e grave ("Commit changes"). O site é reconstruído em cerca de 1 minuto.

| O que quer mudar | Ficheiro |
|---|---|
| Nova versão das tabelas, downloads, contagem de termos, histórico de versões, recursos, parceiros, equipa | `src/data/site.yml` |
| Trabalhos que usam o SECClasS | `src/data/publicacoes.yml` |
| Arquivo de notícias do projeto 2020–2023 | `src/data/noticias.yml` |

**Ao lançar uma nova versão:** (1) publique a release no repositório `secclass`; (2) em `site.yml` atualize `versao_atual`, os `termos` de cada tabela, os links em `downloads` e acrescente um bloco no topo de `versoes`.

PDFs próprios (manuais, artigos): coloque-os em `public/docs/` e indique-os no campo `ficheiro`. Enquanto o ficheiro não existir, o site mostra "em migração" em vez de um link partido.

Logótipos: `public/img/` (SVG gerados a partir do Poppins, em contornos). Falta o logo EEA Grants: coloque-o em `public/img/` e indique-o em `projeto.financiador.logo`.

## Publicações

Para acrescentar um trabalho que aplica o SECClasS, edite `src/data/publicacoes.yml`: copie um bloco existente, preencha título, autores, instituição, local, ano, tipo, resumo, papel do SECClasS e link (DOI de preferência), e grave com `estado: publicado`. O PDF, se o quiser alojar, vai para `public/docs/` e indica-se em `ficheiro`.

## Desenvolvimento local

```bash
npm install
npm run dev        # http://localhost:4321/secclass_site2026/
npm run build      # gera dist/
```

## Passar para o domínio secclass.pt

Opção recomendada: apontar o DNS de `secclass.pt` para o GitHub Pages (*Settings → Pages → Custom domain*), sem servidor próprio para manter.
Neste caso, no `deploy.yml` mude `SITE_URL: https://secclass.pt` e `BASE_PATH: /`.

Os endereços antigos do WordPress (`/tabelas/`, `/search/`, `/sobre/`…) estão redirecionados em `astro.config.mjs`.

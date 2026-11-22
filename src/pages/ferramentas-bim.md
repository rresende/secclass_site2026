---
layout: ../layouts/Pagina.astro
title: Tabelas e ferramentas BIM
description: Tabelas do SECClasS em Excel, para Autodesk Revit e Graphisoft Archicad, Uniformat II em português e exportação da classificação para IFC.
intro: Ficheiros e instruções para classificar modelos BIM com o SECClasS. Todos os ficheiros correspondem à versão 2.0.
---

<nav class="toc" aria-label="Nesta página">
  <a href="#tabelas">Tabelas SECClasS</a>
  <a href="#revit">Autodesk Revit</a>
  <a href="#archicad">Graphisoft Archicad</a>
  <a href="#ifc">Exportação para IFC</a>
  <a href="#uniformat">Uniformat II</a>
</nav>

<h2 id="tabelas">Tabelas SECClasS</h2>

As 13 tabelas do SECClasS (versão 2.0, julho de 2025, correspondente ao Uniclass 2015 de abril de 2025) num único ficheiro Excel, com 17 411 termos.

<div class="dl">
  <a class="btn" href="https://github.com/rresende/secclass/releases/download/V2.0/Tabelas.SECClasS.V2.0.xlsx">Descarregar as tabelas SECClasS v2.0 (.xlsx)</a>
</div>

**Como está organizado o ficheiro:**

- a folha `Introdução` apresenta o sistema e a versão;
- a folha `Todas_Tabelas` junta todos os termos numa só lista, útil para filtrar ou procurar;
- há uma folha por tabela: `Co-Complexos`, `En-Entidades`, `Ac-Atividades`, `SL-Espaços&Locais`, `EF-Elementos&Funções`, `Ss-Sistemas`, `Pr-Produtos`, `Ma-Materiais`, `FI-FormasInformação`, `PM-GestãoProjeto`, `Ro-Agentes`, `TE-Ferramentas&Equipamentos` e `Zz-CAD&Modelação`.

Cada termo tem as colunas **Tabela**, **Código** (ex.: `Ss_25_10_30`), **Título SECClasS**, **Nível** (profundidade na hierarquia, de 2 a 5) e **Título Uniclass** (o termo original em inglês). Os termos acrescentados para a realidade portuguesa estão assinalados na coluna Título Uniclass.

**Alterações da versão 2.0** (consulte as [notas de lançamento](../versoes/v2-0/)):

- Foi traduzida a tabela Ma-Materiais.
- Foram adicionadas traduções dos termos incluídos no Uniclass entre 2022 e abril de 2025, com exceção da tabela Pr-Produtos, onde parte dos novos termos são traduções por IA.
- Revisão das tabelas e adição de termos específicos para Portugal, por solicitação de colegas portugueses. Estas adições estão identificadas na ferramenta de pesquisa online.

**As 13 tabelas e o número de termos:**

| Código | Tabela | Termos |
|---|---|---|
| `Ac` | Atividades | 948 |
| `Ro` | Agentes | 287 |
| `Zz` | CAD | 132 |
| `Co` | Complexos | 417 |
| `EF` | Elementos/funções | 230 |
| `En` | Entidades | 596 |
| `SL` | Espaços/locais | 1 146 |
| `TE` | Ferramentas e equipamentos | 882 |
| `FI` | Formas de informação | 94 |
| `PM` | Gestão de projeto | 1 105 |
| `Ma` | Materiais | 447 |
| `Pr` | Produtos | 8 421 |
| `Ss` | Sistemas | 2 706 |

As tabelas Riscos e Propriedades serão traduzidas numa versão futura. Conheça a função de cada tabela na [página inicial](../#tabelas).

**Manual e vídeos:** descarregue o [manual do sistema SECClasS](../docs/Guia_Utilizacao_SECClasS_V1.0.pdf) (versão 1.0) e veja os vídeos no [canal YouTube do SECClasS](https://youtube.com/playlist?list=PLijhXZogmBZx7DLQw7l8Wzz74_jvXHJMM).

Para procurar um termo sem descarregar o ficheiro, use a [ferramenta de pesquisa](../pesquisa/). Para usar as tabelas no software de modelação, veja as secções [Revit](#revit) e [Archicad](#archicad).

<h2 id="revit">Tabelas para o Autodesk Revit</h2>

Pode classificar modelos BIM de forma expedita usando a ferramenta [Autodesk Standardized Data Tool for Revit](https://interoperability.autodesk.com/) (antigo BIM Interoperability Tools).

<div class="dl">
  <a class="btn" href="https://github.com/rresende/secclass/releases/download/V2.0/SECClasS_V2.0_AutodeskInteroperabilityTools.xlsx">Descarregar as tabelas SECClasS v2.0 para Revit (.xlsx)</a>
</div>

![Exemplo de classificação de elementos no Revit com o Autodesk Standardized Data Tool](../assets/revit-standardized-data-tool.jpg)

**Como usar:** descarregue o [manual de instruções](../docs/Guia_Utilizacao_SECClasS_BIT_v1.0.pdf) (Revit 2022) e veja os [vídeos no canal YouTube do SECClasS](https://youtube.com/playlist?list=PLijhXZogmBZxULushQjF2Y3ZE9T3QOXTw).

Também está disponível a [tabela Uniformat II em português para o Revit](#uniformat).

<h2 id="archicad">Tabelas para o Graphisoft Archicad</h2>

As tabelas da versão 2.0 do SECClasS estão disponíveis no formato de classificação do Archicad (XML).

<div class="dl">
  <a class="btn" href="https://github.com/rresende/secclass/releases/download/V2.0/SECClasS.V2.0.para.Archicad.xml">Descarregar as tabelas SECClasS v2.0 para Archicad (.xml)</a>
</div>

**Como usar:** veja o [vídeo com instruções para o uso das tabelas](https://youtu.be/0sLyCpoQGhI) (2021) no canal YouTube do SECClasS.

As tabelas no formato XML e o vídeo tutorial são fornecidos pela [Infor](https://www.infor.pt/), a quem agradecemos.

<h2 id="ifc">Exportação para IFC</h2>

<p><span class="pill pill-warn">Em actualização</span></p>

O IFC (Industry Foundation Classes) é uma descrição digital normalizada do ambiente construído, incluindo edifícios e infraestruturas. É uma norma internacional aberta ([ISO 16739-1:2024](https://www.iso.org/standard/84123.html)), independente do fornecedor de software, e o principal produto técnico da [buildingSMART International](https://www.buildingsmart.org/) para a promoção do openBIM®.

### Exportação de Revit para IFC

Para exportar para IFC um modelo já classificado no Revit, é necessário mapear os parâmetros de classificação. São necessários os ficheiros:

1. Ficheiro de configuração IFC para os parâmetros do SECClasS — [Secclass_IFC_ParameterSet_PT.txt](https://raw.githubusercontent.com/rresende/secclass/main/ClassificationFiles/IFC_files/Secclass_IFC_ParameterSet_PT.txt)
2. Ficheiro de configuração do projeto — [Secclass_Project_Parameter_PT.txt](https://raw.githubusercontent.com/rresende/secclass/main/ClassificationFiles/IFC_files/Secclass_Project_Parameter_PT.txt)
3. Ficheiro de configuração de layers — [Secclass_exportlayers-ifc-IAI.txt](https://raw.githubusercontent.com/rresende/secclass/main/ClassificationFiles/IFC_files/Secclass_exportlayers-ifc-IAI.txt)

Veja o [vídeo de exportação de Revit para IFC](https://www.youtube.com/watch?v=Kk3WEfh_lvo) no canal YouTube do SECClasS. O manual de instruções está a ser atualizado.

Para abrir ficheiros IFC (.ifc) é necessário um software compatível; existem vários, gratuitos e pagos. No exemplo apresentado usa-se o [Solibri Anywhere](https://www.solibri.com/solibri-anywhere) (gratuito).

### Exportação de Archicad para IFC

Veja o [tutorial em vídeo sobre a exportação de Archicad para IFC](https://www.youtube.com/watch?v=NLxMn_dsgM0&list=PLijhXZogmBZxKa6XdpLqFZLK3lGbrFP6S&index=10), em parceria com a [Infor](https://www.infor.pt/).

<h2 id="uniformat">Uniformat II em português</h2>

O Uniformat 2010 é uma estrutura de decomposição do trabalho (WBS — Work Breakdown Structure) que faz parte do [OmniClass](https://www.csiresources.org/standards/omniclass). É adequado para a elaboração de mapas de quantidades, podendo ser integrado em software de medição nas fases iniciais dos projetos, e está disponível nativamente no Revit. Tem apenas uma tabela de classificação de elementos de construção, pelo que não é um sistema de classificação tal como definido na norma ISO 12006-2.

<div class="dl">
  <a class="btn" href="https://github.com/rresende/secclass/releases/download/v1.0_uniformat/UniformatII_Portugues_V1.0.xlsx">Descarregar Uniformat II em português (.xlsx)</a>
  <a class="btn btn-outline" href="https://github.com/rresende/secclass/releases/download/v1.0_uniformat/UniformatII_Portugues_V1.0_AutodeskClassificationTools.xlsx">Uniformat II para o Revit (.xlsx)</a>
</div>

O Uniformat II está dividido em sete partes, num total de 654 entradas:

- A. Subestrutura
- B. Esqueleto e invólucro
- C. Interiores
- D. Instalações
- E. Equipamento e mobiliário
- F. Construção especial e demolições
- G. Trabalhos na envolvente

O ficheiro Excel tem duas folhas: `Uniformat_2010_EN` (versão original) e `Uniformat_2010_PT` (versão em português europeu). Para usar o Uniformat no Revit, descarregue a tabela para o Revit acima e siga as instruções da [secção Revit](#revit).

O Uniformat II é publicado pelo [Construction Specifications Institute](https://www.csiresources.org/standards/uniformat) e foi traduzido pela [Limsen Consulting](https://limsen.com/) em parceria com a [Lipronerg Engenharia](https://lipronerg.pt/), a quem agradecemos.

---

Comentários, sugestões ou correções: escreva para <a class="eml" href="#" rel="nofollow" data-e="dHAuc3NhbGNjZXNAb2ZuaQ==">info (arroba) secclass.pt</a>.

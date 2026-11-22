import { defineConfig } from 'astro/config';

// SITE_URL e BASE_PATH são definidos no workflow de publicação.
// GitHub Pages:  https://rresende.github.io  +  /secclass_site2026
// Domínio próprio (secclass.pt):  https://secclass.pt  +  /
const site = process.env.SITE_URL || 'https://rresende.github.io';
const base = process.env.BASE_PATH || '/secclass_site2026';

// Endereços do site WordPress antigo -> novos (preserva links externos)
const antigos = {
  '/tabelas': '/#tabelas',
  '/sistemaclassificacao': '/',
  '/lancamentov2-0': '/#versoes',
  '/conhecer-as-tabelas-do-secclass': '/#tabelas',
  '/autodesk-classification-manager': '/#downloads',
  '/tabelas-para-o-graphisoft-archicad': '/#downloads',
  '/uniformatpt': '/#downloads',
  '/exportacao_revit-ifc': '/#downloads',
  '/apps/exportacao-para-ifc': '/#downloads',
  '/apps': '/#downloads',
  '/aprender': '/#recursos',
  '/documentos': '/publicacoes/',
  '/biblioteca-de-objetos-bim': '/#recursos',
  '/regras-de-modelacao-de-objetos-bim': '/#recursos',
  '/sobre': '/#projeto',
  '/about': '/#projeto',
  '/comunidade': '/#comunidade',
  '/noticias-e-eventos': '/arquivo/',
  '/arquivo': '/arquivo/',
  '/search': '/pesquisa/',
  '/termos-condicoes': '/legal/',
  '/politica-de-privacidade': '/legal/',
};
const redirects = Object.fromEntries(
  Object.entries(antigos)
    .filter(([from]) => from !== '/arquivo')
    .map(([from, to]) => [from, base.replace(/\/$/, '') + to]),
);

export default defineConfig({
  site,
  base,
  trailingSlash: 'ignore',
  redirects,
  build: { inlineStylesheets: 'always' },
});

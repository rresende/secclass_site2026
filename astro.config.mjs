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
  '/autodesk-classification-manager': '/#aplicacoes',
  '/tabelas-para-o-graphisoft-archicad': '/#aplicacoes',
  '/uniformatpt': '/#aplicacoes',
  '/exportacao_revit-ifc': '/#aplicacoes',
  '/apps/exportacao-para-ifc': '/#aplicacoes',
  '/apps': '/#aplicacoes',
  '/aprender': '/#recursos',
  '/documentos': '/publicacoes/',
  '/biblioteca-de-objetos-bim': '/#recursos',
  '/regras-de-modelacao-de-objetos-bim': '/#recursos',
  '/sobre': '/#projeto',
  '/about': '/#projeto',
  '/comunidade': '/#manutencao',
  '/noticias-e-eventos': '/arquivo/',
  '/arquivo': '/arquivo/',
  '/search': '/pesquisa/',
  '/legal': '/termos-condicoes/',
  '/menu-de-demonstradores': '/',
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

import fs from 'node:fs';
import path from 'node:path';
import { load as parseYaml } from 'js-yaml';

const dir = path.resolve('src/data');
const load = (f) => parseYaml(fs.readFileSync(path.join(dir, f), 'utf8'));

export const site = load('site.yml');
export const noticias = load('noticias.yml') ?? [];

/** Só as publicações aprovadas aparecem no site. */
export const publicacoes = (load('publicacoes.yml') ?? [])
  .filter((p) => p.estado === 'publicado')
  .sort((a, b) => (b.ano ?? 0) - (a.ano ?? 0) || String(a.titulo).localeCompare(String(b.titulo)));

/** Caminho com o prefixo base (GitHub Pages ou domínio próprio). */
export const url = (p = '') => {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  if (/^https?:|^mailto:/.test(p)) return p;
  return `${base}/${p.replace(/^\//, '')}`;
};

/** PDF local do item, se existir em public/. */
export const pdf = (item) =>
  item.ficheiro && fs.existsSync(path.resolve('public', item.ficheiro)) ? url(item.ficheiro) : null;

/** Resolve o link de um item com "url" externo ou "ficheiro" local em public/. */
export const link = (item) => {
  if (item.ficheiro && fs.existsSync(path.resolve('public', item.ficheiro))) return url(item.ficheiro);
  if (item.url) return item.url;
  return null;
};

export const totalTermos = site.tabelas.reduce((s, t) => s + t.termos, 0);
export const fmt = (n) => n.toLocaleString('pt-PT');

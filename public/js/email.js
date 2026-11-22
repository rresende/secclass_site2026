// Monta os links de email protegidos (ver src/components/Email.astro).
document.querySelectorAll('a.eml[data-e]').forEach(function (a) {
  try {
    var e = atob(a.dataset.e).split('').reverse().join('');
    a.href = 'mailto:' + e + (a.dataset.s ? '?subject=' + encodeURIComponent(a.dataset.s) : '');
    if (!a.dataset.l) a.textContent = e;
  } catch (err) { /* mantém o texto alternativo */ }
});

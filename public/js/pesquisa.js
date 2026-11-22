// Abre a ferramenta de pesquisa já com o termo vindo da caixa da página principal (?q=termo).
(function () {
  var f = document.getElementById('pesquisa-frame');
  var q = new URLSearchParams(location.search).get('q');
  if (!f || !q || !f.dataset.modelo) return;
  f.src = f.dataset.modelo.replace('{termo}', encodeURIComponent(q.trim()));
})();

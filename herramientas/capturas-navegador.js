/* Capturas de página completa desde el navegador (Claude en Chrome).
 *
 * Por qué así: la web suele estar detrás de «Próximamente» y solo se ve con la sesión
 * de administrador abierta en el navegador del estudio. Se carga cada página en un
 * iframe escalado sobre una pantalla del escritorio de WordPress y se hacen capturas
 * de pantalla por tramos, que luego se unen con herramientas/unir_capturas.py.
 *
 * Uso (pegar en la herramienta de JavaScript, en una pestaña del sitio con sesión):
 *   const info = await __rewShot('https://dominio/es/', 1440, 0.3, 700);
 *   // info.secciones -> posición de cada sección (para las marcas numeradas)
 *   // info.pie       -> dónde empieza el pie común (la tira se corta ahí)
 *   // captura de pantalla con save_to_disk
 *   __rewScroll(2333);  // siguiente tramo: altura del tramo = round(viewH / escala)
 *   // captura … y así hasta pasar info.pie
 *   __rewClose();
 *
 * Reglas aprendidas:
 *  - La posición real de cada tramo es la PEDIDA (limitada a altoTotal - tramo). El scrollY
 *    que devuelve el iframe puede venir desplazado unos píxeles: no usarlo para unir.
 *  - El ancho visible de la tira = 1440 × escala (432 px a 0,3). Con viewH = 700 cada tramo
 *    cubre 2333 px de página.
 *  - La ventana del navegador mide ~951 × 713: comprobar innerHeight y usar viewH menor.
 *  - Captura de pantalla a escala 1: con scale < 1 el archivo guardado también se reduce.
 */
window.__rewShot = function (url, ancho, escala, viewH) {
  let o = document.getElementById('rew-shot');
  if (!o) { o = document.createElement('div'); o.id = 'rew-shot'; document.body.appendChild(o); }
  document.documentElement.style.overflow = 'hidden';
  o.style.cssText = 'position:fixed;left:0;top:0;width:100vw;height:100vh;z-index:2147483647;background:#fff;overflow:hidden';
  const H = Math.round(viewH / escala);
  o.innerHTML = '<iframe id="rew-shot-f" src="' + url + '" style="position:absolute;left:0;top:0;width:' + ancho + 'px;height:' + H +
    'px;border:0;transform:scale(' + escala + ');transform-origin:0 0;background:#fff"></iframe>';
  const f = o.querySelector('iframe');
  return new Promise(function (resolve) {
    f.onload = function () {
      const d = f.contentDocument, w = f.contentWindow, st = d.createElement('style');
      // Sin barra de administración, sin aviso de cookies, cabecera no fija y sin animaciones.
      st.textContent = 'html{margin-top:0!important;scrollbar-width:none}html::-webkit-scrollbar{display:none}' +
        '#wpadminbar,[class*="cookieadmin"],[class*="cookie-notice"],[id*="cookie"]{display:none!important}' +
        'header,.site-header,[class*="-head"]{position:relative!important;top:auto!important}' +
        '*,*::before,*::after{transition:none!important;animation:none!important;scroll-behavior:auto!important}';
      d.head.appendChild(st);
      // Elementos que aparecen al hacer scroll: mostrarlos ya (ajustar la clase al tema del cliente).
      d.querySelectorAll('[data-k-reveal],.k-paint,.k-sign,[data-reveal],.reveal').forEach(function (e) { e.classList.add('is-in', 'is-visible'); });
      setTimeout(function () {
        const pies = d.querySelectorAll('footer'), pie = pies[pies.length - 1];
        const main = d.querySelector('main') || d.body;
        const secciones = [].slice.call(main.querySelectorAll('section')).filter(function (s) {
          return !s.parentElement.closest('section') && s.offsetHeight > 80;
        }).map(function (s) {
          const h = s.querySelector('h1,h2');
          return { y: Math.round(s.getBoundingClientRect().top + w.scrollY), alto: s.offsetHeight, titulo: h ? h.textContent.trim().slice(0, 60) : '' };
        });
        resolve({ tramo: H, alto: d.documentElement.scrollHeight, pie: pie ? Math.round(pie.getBoundingClientRect().top + w.scrollY) : null, secciones: secciones });
      }, 1200);
    };
  });
};
window.__rewScroll = function (y) {
  const f = document.getElementById('rew-shot-f');
  f.contentWindow.scrollTo(0, y);
  f.contentDocument.querySelectorAll('[data-k-reveal],.k-paint,.k-sign,[data-reveal],.reveal').forEach(function (e) { e.classList.add('is-in', 'is-visible'); });
  return y;
};
window.__rewClose = function () {
  const o = document.getElementById('rew-shot'); if (o) o.remove();
  document.documentElement.style.overflow = '';
};

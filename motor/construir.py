# -*- coding: utf-8 -*-
"""Resumen estratégico de web · Postsicionate.

Uso:
    python3 motor/construir.py clientes/<cliente>            # HTML + PDF + comprobación
    (la edición «entrega» usa además la hoja `pasos`: capturas con números y los pasos que señalan)
    python3 motor/construir.py clientes/<cliente> --sin-pdf  # solo HTML

Lee clientes/<cliente>/contenido.py y produce:
    clientes/<cliente>/resumen.html
    clientes/<cliente>/entregas/<archivo>-v<version>.pdf
"""
import html, importlib.util, os, sys, asyncio

E = html.escape
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINCEL = ('<svg viewBox="0 0 200 24" preserveAspectRatio="none" aria-hidden="true"><path d="M3 15.5C22 9.5 52 7 86 '
          '7.5S158 8 196 10.5c2 .2 2.8 2.4 1.4 3.7-3.3 2.9-11 4.5-24 5.4-36 2.5-86 3-128 2.4-17-.3-31-1.4-40-3.4-3.6-.8-4-2.6-2.6-3.6z"/></svg>')

# Valores por defecto de la marca: se sobrescriben en MARCA del contenido.
MARCA_BASE = dict(
    tinta='#0F2B4F', texto='#273A52', gris='#5A6B7F', linea='#DCE2EA', papel='#F6F7F9',
    acentos={  # nombre: (color, versión oscura para texto)
        'rojo': ('#FF1F1C', '#C8101A'), 'azul': ('#0181F4', '#0062C4'),
        'verde': ('#009E17', '#007A12'), 'sol': ('#FFC93C', '#9A6400'),
    },
    tricolor=['rojo', 'azul', 'verde'], pincel='sol',
    necesario='#C8101A', recomendado='#0062C4', ok='#009E17', ok_d='#007A12', falta='#FF1F1C',
    titulos=dict(familia='Montserrat', archivos={500: 'fuentes/mont-500.ttf', 600: 'fuentes/mont-600.ttf',
                                                 700: 'fuentes/mont-700.ttf', 800: 'fuentes/mont-800.ttf'}),
    cifras=None,  # ruta a una fuente de dígitos sin solapes (ver herramientas/fuentes.py); None = la de títulos
    css='',       # CSS propio del cliente, después de estilos.css (por ejemplo, titulares en la fuente de su web)
)


def cargar(carpeta):
    spec = importlib.util.spec_from_file_location('contenido', os.path.join(carpeta, 'contenido.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def rel(carpeta, ruta):
    """Ruta de un recurso del repositorio vista desde la carpeta del cliente."""
    return os.path.relpath(os.path.join(RAIZ, ruta), carpeta)


def css_marca(M, carpeta):
    t = M['titulos']
    ff = ''.join(f"@font-face{{font-family:'{t['familia']}';src:url({rel(carpeta, p)}) format('truetype');font-weight:{w}}}\n"
                 for w, p in t['archivos'].items())
    serif = [('Source Serif 4', 'normal', 400, 'fuentes/serif-400.ttf'), ('Source Serif 4', 'italic', 400, 'fuentes/serif-i-400.ttf'),
             ('Source Serif 4', 'italic', 500, 'fuentes/serif-i-500.ttf'), ('Serif Display', 'italic', 400, 'fuentes/serif-i-display.ttf')]
    ff += ''.join(f"@font-face{{font-family:'{f}';src:url({rel(carpeta, p)}) format('truetype');font-weight:{w};font-style:{s}}}\n"
                  for f, s, w, p in serif)
    if M.get('cifras'):
        ff += f"@font-face{{font-family:'Cifras';src:url({M['cifras']}) format('truetype');font-weight:800;unicode-range:U+0030-0039}}\n"
    root = (f":root{{--tinta:{M['tinta']};--texto:{M['texto']};--gris:{M['gris']};--linea:{M['linea']};--papel:{M['papel']};"
            f"--necesario:{M['necesario']};--recomendado:{M['recomendado']};--ok:{M['ok']};--ok-d:{M['ok_d']};--falta:{M['falta']};"
            f"--pincel:{M['acentos'][M['pincel']][0]};"
            f"--sans:'{t['familia']}',ui-sans-serif,system-ui,sans-serif;--serif:'Source Serif 4',Georgia,serif;"
            f"--dig:{'Cifras,' if M.get('cifras') else ''}'{t['familia']}',sans-serif}}\n")
    acc = ''.join(f".a-{n}{{--c:{c};--cd:{d}}}\n" for n, (c, d) in M['acentos'].items())
    acc += f".a-tinta{{--c:{M['tinta']};--cd:{M['tinta']}}}\n"
    tri = ''.join(f".tri i:nth-child({i + 1}){{background:{M['acentos'][n][0]}}}\n" for i, n in enumerate(M['tricolor']))
    return ff + root + acc + tri


class Doc:
    def __init__(self, C, carpeta):
        self.C, self.carpeta = C, carpeta
        self.cli = C.CLIENTE
        self.logo_p = rel(carpeta, 'logos/postsicionate.png')
        self.total = len(C.HOJAS)

    # ---- piezas comunes -------------------------------------------------
    def rh(self):
        return (f'<header class="rh"><img src="{self.logo_p}" alt="Postsicionate">'
                f'<span>{E(self.cli["nombre"])} · {E(self.cli["cabecera"])}</span></header>')

    def ft(self, n):
        return (f'<footer class="ft"><span><span class="tri"><i></i><i></i><i></i></span>{E(self.cli["pie"])}</span>'
                f'<span class="fo">{n:02d}<em>de</em>{self.total:02d}</span></footer>')

    @staticmethod
    def items(lst):
        return ''.join(f'<li><span class="bx"></span><span>{E(t)}</span></li>' for t in lst)

    def checklist(self, need, rec, extra='', lista=None):
        """La lista para marcar. `lista` (edición entrega) cambia los rótulos:
        dict(titulo, nota, grupos=[(rótulo, subtítulo, 'need'|'rec', [puntos])])."""
        if lista:
            out = [f'<section class="chk"><div class="chk-h"><h3>{E(lista["titulo"])}</h3><small>{E(lista.get("nota", "Marque al completar"))}</small></div>']
            for rot, sub, cls, pts in lista['grupos']:
                out.append(f'<div class="grp {cls}"><div class="grp-h"><b>{E(rot)}</b><i>{E(sub)}</i></div><ul>{self.items(pts)}</ul></div>')
            out.append('</section>')
            return ''.join(out)
        out = ['<section class="chk"><div class="chk-h"><h3>Lo que necesitamos de ', E(self.cli['quien']),
               '</h3><small>Marque al completar</small></div>']
        if need:
            out.append(f'<div class="grp need"><div class="grp-h"><b>Necesario</b><i>sin esto la página no se puede terminar</i></div><ul>{self.items(need)}</ul>{extra}</div>')
        if rec:
            out.append(f'<div class="grp rec"><div class="grp-h"><b>Recomendado</b><i>la haría más fuerte</i></div><ul>{self.items(rec)}</ul></div>')
        out.append('</section>')
        return ''.join(out)

    # ---- tipos de hoja --------------------------------------------------
    def portada(self, h, n):
        c = self.cli
        q = E(c['pregunta'])
        if c.get('palabra_pintada'):
            w = E(c['palabra_pintada'])
            q = q.replace(w, f'<span class="paint">{w}{PINCEL}</span>', 1)
        imgs = ''
        if h.get('escritorio'):
            imgs += f'<div class="desk"><img src="{h["escritorio"]}" alt=""></div>'
        if h.get('movil'):
            imgs += f'<div class="phone"><img src="{h["movil"]}" alt=""></div>'
        return f'''<section class="sheet cover a-{h.get('acento', 'sol')}">
<img class="logo-p" src="{self.logo_p}" alt="Postsicionate"><div class="date">{E(c['fecha'])}</div>
<img class="logo-k" src="{c['logo']}" alt="{E(c['nombre'])}">
<div class="qwrap"><span class="lbl" style="color:var(--gris)">{E(h.get('etiqueta', 'La pregunta que guía todo el proyecto'))}</span><p class="q">«{q}»</p></div>
<div class="tblock"><div class="tri"><i></i><i></i><i></i></div><h1 class="tt">{E(h['titulo'])}</h1><p class="st">{E(h['subtitulo'])}</p>
<p class="for">Preparado para {E(c['para'])} <span>· {E(c['cargo'])}</span></p></div>{imgs}</section>'''

    def intro(self, h, n):
        cols = h.get('columnas', ['Lo que necesita ver', 'Cómo lo mostramos', 'Ya lo tenemos', 'Nos falta'])
        anchos = h.get('anchos', [21, 31, 23, 25] if len(cols) == 4 else [round(100 / len(cols))] * len(cols))
        cg = ''.join(f'<col style="width:{w}%">' for w in anchos)
        if h.get('marcas_columnas', True) and len(cols) == 4:
            # Edición de revisión: «lo tenemos» en verde y «falta» con su casilla.
            rows = ''.join(
                f'<tr><td><small>{i + 1:02d}</small>{E(a)}</td><td>{E(b)}</td><td class="has"><span class="sq on"></span>{E(c)}</td>'
                f'<td class="miss"><span class="sq off"></span>{E(d)}</td></tr>' for i, (a, b, c, d) in enumerate(h['filas']))
            head = f'<th>{E(cols[0])}</th><th>{E(cols[1])}</th><th><span class="sq on"></span>{E(cols[2])}</th><th><span class="sq off"></span>{E(cols[3])}</th>'
        else:
            # Edición de entrega: texto llano en todas las columnas.
            rows = ''.join('<tr>' + ''.join(f'<td>{"<small>%02d</small>" % (i + 1) if j == 0 else ""}{E(c)}</td>' for j, c in enumerate(f)) + '</tr>'
                           for i, f in enumerate(h['filas']))
            head = ''.join(f'<th>{E(c)}</th>' for c in cols)
        cj = h.get('caja')
        if cj:
            notas = ''.join(f'<p class="{"n" if k == 0 else "r"}"><b>{E(a)}</b>{E(b)}</p>' for k, (a, b) in enumerate(cj.get('notas', [])))
            caja = (f'<div class="howto"><h3>{E(cj["titulo"])}</h3><p>{E(cj["texto"])}</p>'
                    f'<div style="display:grid;gap:10px">{notas}</div></div>')
        else:
            caja = f'''<div class="howto"><h3>Cómo leer las hojas siguientes</h3>
<p>Cada hoja explica una página de la web: la pregunta que responde, la lógica de su estructura y una lista para marcar con lo que necesitamos de {E(self.cli['quien'])}.</p>
<div style="display:grid;gap:10px"><p class="n"><b>Necesario</b>Sin esto la página no se puede terminar: datos, confirmaciones, permisos y aprobaciones.</p><p class="r"><b>Recomendado</b>La haría más fuerte. Cada recomendación explica por qué.</p></div></div>'''
        return f'''<section class="sheet intro a-{h.get('acento', 'rojo')}">{self.rh()}<div class="body">
<p class="kick">{E(h.get('antetitulo', 'Introducción'))}</p><h1 class="h1">{E(h['titulo'])}</h1><p class="lead">{E(h['entrada'])}</p>
<table class="tt-table"><colgroup>{cg}</colgroup>
<thead><tr>{head}</tr></thead>
<tbody>{rows}</tbody></table>
{caja}
</div>{self.ft(n)}</section>'''

    def principios(self, h, n):
        cells = ''.join(f'<article class="a-{c}"><div class="pn">{i + 1:02d}</div><h3>{E(t)}</h3><p>{E(d)}</p></article>'
                        for i, (c, t, d) in enumerate(h['items']))
        mapa = ''
        if h.get('mapa'):
            m = h['mapa']
            def li(x):
                nombre, hecha = x[0], x[1]
                nota = f'<small>{E(x[2])}</small>' if len(x) > 2 and x[2] else ''
                hijos = ''
                if len(x) > 3 and x[3]:
                    hijos = '<ul>' + ''.join(f'<li><span class="ss{"" if hh else " off"}"></span>{E(nn)}</li>' for nn, hh in x[3]) + '</ul>'
                return f'<li><span class="ss{"" if hecha else " off"}"></span>{E(nombre)}{nota}{hijos}</li>'
            movil = ''
            if h.get('movil'):
                movil = f'<div class="a-{h.get("acento_movil", "sol")}"><div class="phone-s"><img src="{h["movil"]}" alt=""></div><p class="cap">{h.get("pie_movil", "")}</p></div>'
            leyenda = ('<div class="legend"><span><span class="ss"></span>Construida</span><span><span class="ss off"></span>Próxima</span></div>'
                       if m.get('leyenda', True) else '')
            mapa = (f'<div class="mapz"><div class="map"><span class="lbl">{E(m.get("etiqueta", "Mapa de la web"))}</span><h3>{E(m["titulo"])}</h3>'
                    f'<p class="note">{E(m["nota"])}</p><ul class="tree">{"".join(li(x) for x in m["arbol"])}</ul>'
                    f'{leyenda}</div>'
                    f'{movil}</div>')
        return f'''<section class="sheet a-{h.get('acento', 'azul')}">{self.rh()}<div class="body">
<p class="kick">{E(h.get('antetitulo', 'Principios'))}</p><h1 class="h1">{E(h['titulo'])}</h1><div class="prin">{cells}</div>{mapa}
</div>{self.ft(n)}</section>'''

    def pagina(self, p, n):
        alto = p['alto_tira']  # alto en píxeles de la imagen de la tira
        esc = p.get('escala', 0.3)
        # Una marca None es un punto que no está en la captura (sale en otra página).
        # Una marca (y, x) se coloca además a x % del ancho de la tira (por defecto, en su borde izquierdo).
        def marca(i, m):
            if isinstance(m, (tuple, list)):
                y, x = m
                return f'<span class="mk" style="top:{y * esc / alto * 100:.2f}%;left:calc({x}% - 11px)">{i + 1}</span>'
            return f'<span class="mk" style="top:{m * esc / alto * 100:.2f}%">{i + 1}</span>'
        marks = ''.join(marca(i, m) for i, m in enumerate(p['marcas']) if m is not None)
        def sin_marca(i):
            return i >= len(p['marcas']) or p['marcas'][i] is None
        logic = ''.join(
            f'<li><span class="mk{" nm" if sin_marca(i) else ""}">{i + 1}</span><div><b>{E(t)}</b><p>{E(d)}</p></div></li>'
            for i, (t, d) in enumerate(p['logica']))
        extra = ''
        if p.get('fotos'):
            figs = ''.join(f'<figure><img src="{src}" alt=""><figcaption>{E(cap)}</figcaption><span class="wl">Año</span><span class="wl">Lugar</span></figure>'
                           for src, cap in p['fotos'])
            extra = f'<div class="fphotos">{figs}</div>'
        cap = p.get('pie_tira', '<b>La página completa, vista en ordenador.</b> Los números señalan cada punto de «La lógica».')
        return f'''<section class="sheet a-{p['acento']}">{self.rh()}<div class="body"><div class="pg" style="--sw:{p.get('ancho_tira', 182)}px">
<div class="pg-main">
  <div class="pg-top"><div class="pnum">{p['n']}</div><div><p class="kick">{E(p.get('antetitulo', 'Página de la web'))}</p><h1 class="h1">{E(p['nombre'])}</h1><p class="url">{E(p['url'])}</p></div></div>
  <div class="pq"><span class="lbl">{E(p.get('etiqueta_pregunta', self.cli.get('etiqueta_pregunta', 'La pregunta que responde')))}</span><p class="q">«{E(p['pregunta'])}»</p></div>
  <div class="logic"><span class="lbl">{E(p.get('titulo_logica', 'La lógica'))}</span><ol>{logic}</ol></div>
  {f'<div class="acc"><b>{E(p["nota"][0])}</b><p>{E(p["nota"][1])}</p></div>' if p.get('nota') else ''}{self.checklist(p.get('necesario', []), p.get('recomendado', []), extra, p.get('lista'))}
</div>
<aside class="pg-side"><div class="strip-w"><div class="strip"><img src="{p['tira']}" alt=""></div>{marks}</div><p class="cap">{cap}</p></aside>
</div></div>{self.ft(n)}</section>'''

    def herramienta(self, h, n):
        does = ''.join(f'<li>{E(x)}</li>' for x in h['puede'])
        shots = ''
        if h.get('capturas'):
            s = h['capturas']
            shots = '<div class="shots">' + ''.join(f'<div class="s{i + 1}"><img src="{x}" alt=""></div>' for i, x in enumerate(s[:2])) + '</div>'
        tabla = ''
        if h.get('tabla'):
            t = h['tabla']
            heads = ''.join(f'<th class="{"c" if i >= 2 else ""}">{E(x)}</th>' for i, x in enumerate(t['columnas']))
            cols = ''.join(f'<col style="width:{w}%">' for w in t['anchos'])
            body = ''
            for f in t['filas']:
                av = f'<img src="{f["avatar"]}" alt="">' if f.get('avatar') else ''
                celdas = ''
                for v in f['casillas']:
                    celdas += f'<td class="c" colspan="{v[1]}"><span class="own">{E(v[0])}</span></td>' if isinstance(v, tuple) else '<td class="c"><span class="bx"></span></td>'
                body += f'<tr class="a-{f.get("acento", "tinta")}"><td class="who">{av}{E(f["nombre"])}</td><td>{E(f["detalle"])}</td>{celdas}</tr>'
            tabla = (f'<div style="margin-top:20px"><span class="lbl">{E(t["titulo"])}</span><table class="team-t"><colgroup>{cols}</colgroup>'
                     f'<thead><tr>{heads}</tr></thead><tbody>{body}</tbody></table></div>')
        nota = f'<div class="acc"><b>{E(h["nota"][0])}</b><p>{E(h["nota"][1])}</p></div>' if h.get('nota') else ''
        return f'''<section class="sheet tool a-{h.get('acento', 'sol')}">{self.rh()}<div class="body">
<p class="kick">{E(h.get('antetitulo', 'Para el cliente'))}</p><h1 class="h1">{E(h['titulo'])}</h1><p class="lead">{E(h['entrada'])}</p>
<div class="pn-grid"><div><span class="lbl">{E(h.get('titulo_puede', 'Lo que se puede hacer'))}</span><ul class="does">{does}</ul></div>{shots}</div>
{tabla}{nota}</div>{self.ft(n)}</section>'''

    def pasos(self, h, n):
        """Edición de entrega: una o varias capturas con números encima y los pasos que señalan.

        capturas=[dict(src, ancho=% del ancho útil, marcas=[(x %, y %, número)], pie='…', marco='panel'|'web')]
        pasos=[(título, texto)]  -> numerados 1…n, como las marcas
        lado=True               -> capturas a la derecha (columna de `ancho_lado` px) y pasos a la izquierda
        capturas_lado=[…]       -> con lado=True: `capturas` en una fila arriba y estas junto a los pasos
        """
        def figuras(lista):
            out = ''
            for c in lista:
                mk = ''.join(f'<span class="mk" style="left:{x}%;top:{y}%">{k}</span>' for x, y, k in c.get('marcas', []))
                pie = f'<figcaption>{c["pie"]}</figcaption>' if c.get('pie') else ''
                out += (f'<figure class="g-fig {c.get("marco", "panel")}" style="width:{c.get("ancho", 100)}%">'
                        f'<div class="g-shot"><img src="{c["src"]}" alt="">{mk}</div>{pie}</figure>')
            return out
        figs = figuras(h.get('capturas', []))
        cols = h.get('columnas_pasos', 2 if not h.get('lado') else 1)
        steps = ''.join(f'<li><span class="mk">{i + 1}</span><div><b>{E(t)}</b><p>{E(d)}</p></div></li>' for i, (t, d) in enumerate(h['pasos']))
        nota = f'<div class="acc"><b>{E(h["nota"][0])}</b><p>{E(h["nota"][1])}</p></div>' if h.get('nota') else ''
        lista = self.checklist([], [], '', h['lista']) if h.get('lista') else ''
        if h.get('lado'):
            # Con `capturas_lado`, `capturas` va en una fila arriba y `capturas_lado` junto a los pasos.
            arriba, junto = ('', figs) if 'capturas_lado' not in h else (f'<div class="g-figs">{figs}</div>' if figs else '', figuras(h['capturas_lado']))
            cuerpo = (f'{arriba}<div class="g-lado" style="--gl:{h.get("ancho_lado", 330)}px"><ol class="g-steps c1">{steps}</ol>'
                      f'<div class="g-figs col">{junto}</div></div>')
        else:
            cuerpo = f'<div class="g-figs">{figs}</div><ol class="g-steps c{cols}">{steps}</ol>'
        return f'''<section class="sheet guide a-{h.get('acento', 'sol')}">{self.rh()}<div class="body">
<p class="kick">{E(h.get('antetitulo', 'Paso a paso'))}</p><h1 class="h1">{h['titulo'] if h.get('titulo_html') else E(h['titulo'])}</h1><p class="lead">{E(h['entrada'])}</p>
{cuerpo}{nota}{lista}</div>{self.ft(n)}</section>'''

    def proximas(self, h, n):
        blocks = ''
        for b in h['bloques']:
            li = ''
            if b.get('necesario'):
                li += f'<span class="tag">Necesario</span><ul>{self.items(b["necesario"])}</ul>'
            if b.get('recomendado'):
                li += f'<span class="tag r">Recomendado</span><ul>{self.items(b["recomendado"])}</ul>'
            blocks += f'<article class="nx"><h3>{E(b["titulo"])}<em>{E(b["etiqueta"])}</em></h3><p>{E(b["texto"])}</p>{li}</article>'
        extra = ''
        if h.get('lista'):
            l = h['lista']
            extra = (f'<section class="shotlist"><div class="sl-h"><div><span class="lbl" style="color:var(--recomendado)">{E(l["antetitulo"])}</span>'
                     f'<h3>{E(l["titulo"])}</h3></div><p>{E(l["texto"])}</p></div><ul>{self.items(l["items"])}</ul></section>')
        return f'''<section class="sheet a-{h.get('acento', 'azul')}">{self.rh()}<div class="body">
<p class="kick" style="color:var(--recomendado)">Próximas entregas</p><h1 class="h1">{E(h['titulo'])}</h1>
<p class="lead" style="margin-top:12px;max-width:640px">{E(h['entrada'])}</p><div class="next-grid">{blocks}</div>{extra}
</div>{self.ft(n)}</section>'''

    def revision(self, h, n):
        cells = ''.join(f'<article class="a-{c}"><div class="pn">{i + 1:02d}</div><h3>{E(t)}</h3><p>{E(d)}</p></article>'
                        for i, (c, t, d) in enumerate(h['pasos']))
        boxes = ''.join(f'<div class="bxx a-{c}"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for c, t, d in h['cajas'])
        # La ruta y las líneas para notas son opcionales: sin `ruta` o con lineas_notas=0 no salen.
        ruta = h.get('ruta') or []
        rl = ''.join(f'<li class="{"now" if i == h.get("paso_actual", 0) else ""}"><span>{i + 1:02d}</span>{E(x)}</li>' for i, x in enumerate(ruta))
        cols = '' if len(ruta) == 5 else f' style="grid-template-columns:repeat({len(ruta)},minmax(0,1fr))"'
        road = (f'<div class="road"><span class="lbl" style="color:var(--recomendado)">{E(h.get("titulo_ruta", "Próximos pasos"))}</span><ol{cols}>{rl}</ol></div>'
                if ruta else '')
        n_lineas = h.get('lineas_notas', 6)
        notas = (f'<div class="notes"><span class="lbl" style="color:var(--gris)">{E(h.get("titulo_notas", "Notas de la revisión"))}</span>'
                 + '<div class="ln"></div>' * n_lineas + '</div>') if n_lineas else ''
        return f'''<section class="sheet a-{h.get('acento', 'azul')}">{self.rh()}<div class="body">
<p class="kick">{E(h.get('antetitulo', 'Primera revisión'))}</p><h1 class="h1">{E(h['titulo'])}</h1>
<div class="steps">{cells}</div><div class="boxes">{boxes}</div>
{road}{notas}
<div class="sign"><p>{E(h['firma'])}</p><img src="{self.logo_p}" alt="Postsicionate"></div>
</div>{self.ft(n)}</section>'''

    def html(self):
        M = dict(MARCA_BASE)
        M.update(getattr(self.C, 'MARCA', {}))
        css = css_marca(M, self.carpeta) + open(os.path.join(RAIZ, 'motor', 'estilos.css'), encoding='utf-8').read() + M.get('css', '')
        hojas = [getattr(self, h['tipo'])(h, i + 1) for i, h in enumerate(self.C.HOJAS)]
        return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{E(self.cli["nombre"])} · {E(self.cli["cabecera"])}</title>'
                f'<style>{css}</style></head><body>{"".join(hojas)}</body></html>')


async def a_pdf(html_path, pdf_path, meta):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto('file://' + os.path.abspath(html_path))
        await pg.evaluate('document.fonts.ready')
        await pg.wait_for_timeout(400)
        # Comprobación: ningún elemento puede salirse del área útil de su hoja.
        fuera = await pg.evaluate('''() => [...document.querySelectorAll('.sheet')].map((s, i) => {
            const b = s.querySelector('.body'); if (!b) return null;
            const lim = b.getBoundingClientRect().bottom + 1; let peor = 0;
            b.querySelectorAll('*').forEach(e => { const r = e.getBoundingClientRect(); if (r.height > 0 && r.bottom > lim) peor = Math.max(peor, r.bottom - lim); });
            return peor > 0 ? `Hoja ${i + 1}: se sale ${Math.round(peor)} px` : null; }).filter(Boolean)''')
        tmp = pdf_path + '.tmp'
        await pg.pdf(path=tmp, format='Letter', print_background=True, prefer_css_page_size=True)
        await b.close()
    from pypdf import PdfReader, PdfWriter
    r, w = PdfReader(tmp), PdfWriter()
    for page in r.pages:
        w.add_page(page)
    w.add_metadata(meta)
    w.write(pdf_path)
    os.remove(tmp)
    return fuera, len(r.pages)


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    carpeta = os.path.abspath(sys.argv[1])
    C = cargar(carpeta)
    doc = Doc(C, carpeta)
    html_path = os.path.join(carpeta, 'resumen.html')
    open(html_path, 'w', encoding='utf-8').write(doc.html())
    print('HTML:', os.path.relpath(html_path))
    if '--sin-pdf' in sys.argv:
        return
    c = C.CLIENTE
    os.makedirs(os.path.join(carpeta, 'entregas'), exist_ok=True)
    pdf = os.path.join(carpeta, 'entregas', f"{c['archivo']}-v{c['version']}.pdf")
    fuera, n = asyncio.run(a_pdf(html_path, pdf, {'/Title': f"{c['nombre']} · {c['cabecera']}", '/Author': 'Postsicionate',
                                                   '/Subject': c.get('asunto', ''), '/Creator': 'Postsicionate'}))
    print(f'PDF: {os.path.relpath(pdf)} ({n} hojas)')
    if n != doc.total:
        print(f'AVISO: se esperaban {doc.total} hojas y salieron {n}: alguna hoja se desborda.')
    for f in fuera:
        print('AVISO:', f)
    if not fuera and n == doc.total:
        print('Comprobación: todo dentro de su hoja.')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""Une los tramos capturados en una tira de página completa.

Uso:
    python3 herramientas/unir_capturas.py manifiesto.json clientes/<cliente>/img

manifiesto.json:
{
  "escala": 0.3, "ancho": 1440, "viewH": 700,
  "paginas": {
    "inicio": {"alto_total": 7686, "pie": 6732,
               "tramos": [["/ruta/captura-1.jpg", 0], ["/ruta/captura-2.jpg", 2333], ["/ruta/captura-3.jpg", 4666]]}
  }
}
Cada tramo es [archivo, scroll PEDIDO]. Si el pedido supera alto_total - tramo, se limita solo.
Imprime el alto de cada tira: es el valor `alto_tira` de la hoja en contenido.py.
"""
import json, os, sys
from PIL import Image


def main():
    man = json.load(open(sys.argv[1]))
    dest = sys.argv[2]
    os.makedirs(dest, exist_ok=True)
    s, ancho, vh = man['escala'], man['ancho'], man['viewH']
    W = round(ancho * s)
    tramo = round(vh / s)
    for nombre, p in man['paginas'].items():
        fin = p.get('pie') or p['alto_total']
        H = round(fin * s)
        out = Image.new('RGB', (W, H), 'white')
        for archivo, y in p['tramos']:
            y = min(y, p['alto_total'] - tramo)  # el navegador no deja pasar del final
            im = Image.open(archivo).convert('RGB').crop((0, 0, W, vh))
            out.paste(im, (0, round(y * s)))
        out = out.crop((0, 0, W, H))
        ruta = os.path.join(dest, f'strip-{nombre}.jpg')
        out.save(ruta, quality=92)
        print(f'{nombre}: {ruta} · alto_tira={H}')


if __name__ == '__main__':
    main()

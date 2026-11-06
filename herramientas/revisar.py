# -*- coding: utf-8 -*-
"""Hojas de contacto para revisar el PDF con los ojos (3 páginas por imagen).

Uso:
    python3 herramientas/revisar.py clientes/<cliente>/entregas/<archivo>.pdf [carpeta_salida]
Necesita pdftoppm (poppler). Revisar SIEMPRE las imágenes antes de entregar: la comprobación
automática detecta desbordes, no textos que quedan sueltos, fotos mal recortadas o huecos.
"""
import glob, os, subprocess, sys, tempfile
from PIL import Image


def main():
    pdf = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(pdf), 'revision')
    os.makedirs(out, exist_ok=True)
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-r', '80', '-png', pdf, os.path.join(tmp, 'p')], check=True)
    pags = sorted(glob.glob(os.path.join(tmp, 'p-*.png')))
    for i in range(0, len(pags), 3):
        ims = [Image.open(p) for p in pags[i:i + 3]]
        w, h = ims[0].size
        hoja = Image.new('RGB', (w * len(ims) + 20 * (len(ims) - 1), h), '#888')
        for j, im in enumerate(ims):
            hoja.paste(im, (j * (w + 20), 0))
        ruta = os.path.join(out, f'hojas-{i + 1:02d}-{i + len(ims):02d}.png')
        hoja.save(ruta)
        print(ruta)


if __name__ == '__main__':
    main()

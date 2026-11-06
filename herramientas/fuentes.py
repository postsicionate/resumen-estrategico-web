# -*- coding: utf-8 -*-
"""Prepara las fuentes de un cliente para el PDF.

Por qué: Chrome inserta las fuentes VARIABLES como «Type 3», que algunos visores e
impresoras muestran menos nítidas. Con instancias estáticas se insertan como TrueType.
Además, algunas fuentes variables (Montserrat, por ejemplo) dibujan los dígitos con
contornos que se cruzan: con relleno no se nota, pero con contorno (los números grandes
del resumen) se ven líneas internas. Por eso se genera una fuente de solo dígitos sin solapes.

Uso:
    python3 herramientas/fuentes.py titulos <fuente-variable.woff2|ttf> <carpeta> <prefijo>
        -> <prefijo>-500.ttf … <prefijo>-800.ttf
    python3 herramientas/fuentes.py cifras <fuente-variable> <salida.ttf> [peso=800]
        -> fuente de solo dígitos 0-9, sin solapes (para MARCA['cifras'])
"""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset


def estatica(src, ejes):
    f = TTFont(src)
    if 'fvar' in f:
        f = instancer.instantiateVariableFont(f, ejes, updateFontNames=False)
    f.flavor = None
    return f


def main():
    modo = sys.argv[1]
    if modo == 'titulos':
        src, carpeta, pref = sys.argv[2], sys.argv[3], sys.argv[4]
        os.makedirs(carpeta, exist_ok=True)
        for w in (500, 600, 700, 800):
            ruta = os.path.join(carpeta, f'{pref}-{w}.ttf')
            estatica(src, {'wght': w}).save(ruta)
            print(ruta)
    elif modo == 'cifras':
        src, out = sys.argv[2], sys.argv[3]
        peso = int(sys.argv[4]) if len(sys.argv) > 4 else 800
        f = estatica(src, {'wght': peso})
        from fontTools.ttLib.removeOverlaps import removeOverlaps
        removeOverlaps(f)
        opts = subset.Options(); opts.name_IDs = ['*']; opts.notdef_outline = True
        s = subset.Subsetter(opts); s.populate(text='0123456789'); s.subset(f)
        f.save(out)
        print(out)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()

# Resumen estratégico de web · Postsicionate

El documento PDF que acompaña la presentación de una web al cliente. Explica, página por página, la lógica detrás de la estructura y el diseño, y termina cada hoja con una lista para marcar lo que necesitamos del cliente para terminar.

El primer caso es Kids Palace Academy (noviembre de 2026). Está completo en `clientes/kids-palace-academy/` y sirve de ejemplo de cada tipo de hoja de la edición de revisión. La primera edición de entrega es la guía del panel de King Black (`clientes/king-black/`, noviembre de 2026): las mismas hojas, con instrucciones de uso en lugar de listas de pendientes, y la hoja `pasos`.

## La idea en una frase

Toda la web responde **una pregunta** que se hace quien compra. Por ejemplo, en Kids Palace: «¿Por qué debo confiar en esta institución para el cuidado y la educación inicial de mis hijos?». El resumen muestra cómo cada página la responde y qué falta para responderla del todo.

## Las tres ediciones

| Edición | Cuándo | Qué lleva |
| --- | --- | --- |
| Propuesta | Antes de construir | La pregunta guía, el mapa, la lógica prevista de cada página y lo que necesitamos para empezar |
| Primera revisión | Con la web construida, detrás de «Próximamente» | Lo de Kids Palace: la lógica sobre capturas reales y las listas «Necesario / Recomendado» |
| Entrega | Al lanzar | Lo que se entrega, los accesos, cómo usar los paneles y qué mantener |

## Cómo se pide

En cualquier proyecto, a Claude: «Prepara el resumen estratégico de [cliente], edición [propuesta / revisión / entrega]». La habilidad «resumen-estrategico-web» contiene el método y las reglas. Este repositorio contiene la plantilla y las herramientas.

## Qué hay aquí

```
motor/construir.py      Genera el HTML y el PDF a partir del contenido de un cliente
motor/estilos.css       Diseño de las hojas (tamaño carta)
herramientas/           Capturas desde el navegador, unión de capturas, fuentes y revisión visual
fuentes/                Montserrat y Source Serif 4 en versiones fijas (licencia OFL)
logos/postsicionate.png Logo del estudio
clientes/<cliente>/     contenido.py, imágenes (img/) y PDF entregados (entregas/)
```

## Tipos de hoja

`portada` · `intro` (la pregunta y la tabla «lo que necesita ver / cómo lo mostramos / lo tenemos / falta») · `principios` (decisiones de diseño y mapa de la web) · `pagina` (una por página de la web: pregunta, lógica numerada sobre la captura completa y lista para marcar) · `herramienta` (paneles que gestiona el cliente, con tabla para marcar) · `proximas` (lo que falta por construir) · `revision` (cómo revisar y próximos pasos) · `pasos` (edición de entrega: capturas con números encima y los pasos que señalan).

Para la edición de entrega, las hojas admiten rótulos propios (todos opcionales; sin ellos salen como en Kids Palace):

- `intro`: `antetitulo`, `columnas` de 3 o 4, `anchos`, `marcas_columnas=False` (texto llano, sin «lo tenemos / falta») y `caja` (título, texto y dos notas) en lugar de «Cómo leer las hojas siguientes».
- `principios`: `antetitulo`; en el mapa, `etiqueta` y `leyenda=False`.
- `pagina`: `antetitulo`, `titulo_logica`, `nota` (una caja antes de la lista), `lista` (título, nota y grupos propios en lugar de «Necesario / Recomendado») y marcas `None` (el punto no está en la captura) o `(y, x)` (la marca a x % del ancho de la tira).
- `pasos`: `capturas` con `marcas=[(x %, y %, número)]`, `marco='panel'|'web'` y `pie`; `lado=True` con `capturas_lado` para poner una captura junto a los pasos; `nota` y `lista`.
- `revision`: `titulo_ruta` (con cualquier número de pasos) y `titulo_notas`.
- `MARCA['css']`: CSS propio del cliente, después de `estilos.css` (por ejemplo, los titulares en la fuente de su web).

## Pasos técnicos

1. **Capturas**: en el navegador con la sesión del sitio abierta, cargar `herramientas/capturas-navegador.js` y capturar cada página por tramos (instrucciones dentro del archivo). Unir con `herramientas/unir_capturas.py`.
2. **Contenido**: copiar `clientes/kids-palace-academy/contenido.py` a la carpeta del cliente nuevo y reescribirlo.
3. **Fuentes de marca** (si el cliente no usa Montserrat): `herramientas/fuentes.py`.
4. **Construir**: `python3 motor/construir.py clientes/<cliente>`. Avisa si algo se sale de su hoja.
5. **Revisar con los ojos**: `python3 herramientas/revisar.py clientes/<cliente>/entregas/<archivo>.pdf`.
6. **Versión en el nombre del archivo**: cada entrega sube `version` en `CLIENTE`.

Requisitos: Python 3 con `playwright`, `pypdf`, `Pillow` y `fonttools`; `pdftoppm` (poppler). Para `herramientas/fuentes.py`: `brotli` (fuentes en woff2) y `skia-pathops` (cifras sin solapes). Las fuentes de Google se consiguen con `npm pack @fontsource/<fuente>` (o `@fontsource-variable/<fuente>`).

Capturas del escritorio de WordPress (edición de entrega): cargar la pantalla en un iframe de 1100 px escalado a 1,3 sobre una pestaña del sitio y guardar con la acción `zoom` de la herramienta del navegador, que da PNG nítido (la captura normal es JPEG). Con la sesión del usuario del cliente, para que salga su menú.

## Fuentes

Montserrat y Source Serif 4 se distribuyen con la SIL Open Font License 1.1, que permite usarlas, modificarlas e incluirlas en documentos. Las fuentes de cada cliente van en su carpeta con su licencia (King Black: Archivo y Libre Caslon Text, también OFL).

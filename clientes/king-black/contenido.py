# -*- coding: utf-8 -*-
# King Black Tour & Travel · Guía rápida del panel para Yobi (edición de entrega, noviembre de 2026).
# Primer caso de la edición «entrega»: usa la hoja `pasos` (capturas con números y los pasos que señalan).
# Las marcas de las capturas van en % del ancho y del alto de cada imagen: (x, y, número del paso).

CLIENTE = dict(
    nombre='King Black Tour & Travel',
    cabecera='Guía rápida de su panel',
    pie='Guía de uso · Noviembre de 2026',
    fecha='Noviembre de 2026',
    logo='img/logo-kb.png',
    para='Yobi Junior', cargo='Anfitrión de King Black Tour & Travel',
    quien='usted',
    pregunta='¿Cómo mantengo mi web al día yo mismo?',
    palabra_pintada='yo mismo',
    etiqueta_pregunta='La pregunta que responde esta hoja',
    archivo='guia-panel-king-black-yobi', version='3.1',
    asunto='Guía rápida del panel de kingblacktour.com',
)

F = 'clientes/king-black/fuentes/'
MARCA = dict(
    # Negro noche y oro, como la web. Sobre papel blanco el oro se usa en filetes, marcos y sombras;
    # para texto, su versión oscura.
    tinta='#0B1620', texto='#27323A', gris='#66737B', linea='#E4DED2', papel='#F6F1E8',
    acentos={
        'oro': ('#D4AF37', '#8A6A14'),
        'noche': ('#0E1E29', '#0E1E29'),
        'champan': ('#EBD489', '#8A6A14'),   # solo para el pincel y la tercera raya
        'bronce': ('#B8923A', '#7A5C0F'),
    },
    tricolor=['noche', 'oro', 'champan'], pincel='champan',
    necesario='#8A6A14', recomendado='#0E1E29', ok='#8A6A14', ok_d='#8A6A14', falta='#8A6A14',
    # Archivo, la letra de las etiquetas y los botones de la web; los titulares, en Libre Caslon, como la web.
    titulos=dict(familia='Archivo', archivos={500: F + 'archivo-500.ttf', 600: F + 'archivo-600.ttf',
                                              700: F + 'archivo-700.ttf', 800: F + 'archivo-800.ttf'}),
    cifras='fuentes/archivo-cifras.ttf',
    css='''
@font-face{font-family:'Caslon';src:url(fuentes/caslon-400.ttf) format('truetype');font-weight:400;font-style:normal}
@font-face{font-family:'Caslon';src:url(fuentes/caslon-i-400.ttf) format('truetype');font-weight:400;font-style:italic}
@font-face{font-family:'Caslon';src:url(fuentes/caslon-700.ttf) format('truetype');font-weight:700;font-style:normal}
.h1{font-family:'Caslon',Georgia,serif;font-weight:400;font-size:32px;line-height:1.1;letter-spacing:-.012em}
.cover .q{font-family:'Caslon',Georgia,serif;font-style:italic;font-size:36px;line-height:1.18;letter-spacing:-.01em}
.cover .tt{font-family:'Caslon',Georgia,serif;font-weight:400;font-size:30px;letter-spacing:-.01em}
.cover .logo-k{top:100px;left:60px;height:92px}
.cover .qwrap{top:218px}
.pq .q{font-family:'Caslon',Georgia,serif;font-style:italic;font-weight:400;font-size:19px}
.tt-table td:first-child{font-weight:700}
.tree small{font-size:9.5px}
.intro .tt-table td{padding-top:11px;padding-bottom:12px;font-size:11px}
.intro .tt-table td:first-child{font-size:11.5px}
.intro .howto{margin-top:26px}
''',
)

# Marcas de la captura de la Galería (se fijan al hacer la captura).
GALERIA_MARCAS = [(47, 8, 2), (95.5, 8, 5), (7.7, 88, 2), (18.4, 88, 4), (43, 50, 3)]

HOJAS = [
    dict(tipo='portada', acento='oro',
         etiqueta='La pregunta que responde esta guía',
         titulo='Guía rápida de su panel',
         subtitulo='Lo que usted puede cambiar en kingblacktour.com: dónde se hace, cómo se hace y dónde aparece en la web.',
         escritorio='img/portada-panel.png', movil='img/movil-saona.jpg'),

    dict(tipo='intro', acento='oro', antetitulo='Su panel de un vistazo',
         titulo='Usted escribe, la web lo publica',
         entrada='Su panel es un formulario. Usted rellena los datos de cada excursión, de cada paquete y de las fotos de la portada, y en unos segundos la web los publica con su diseño de siempre. Esta tabla le dice dónde se cambia cada cosa y dónde la ven sus clientes.',
         columnas=['Lo que quiere cambiar', 'Dónde se hace, en su panel', 'Dónde se ve en la web'],
         anchos=[29, 38, 33], marcas_columnas=False,
         filas=[
             ('El precio de una excursión', 'Excursiones → la excursión → pestaña «Tarjeta» → «Precio»', 'En su tarjeta de Experiences, en su página y en Google, a la vez'),
             ('Textos, fotos y vídeos de una excursión', 'Excursiones → la excursión → sus siete pestañas', 'En la página de la excursión'),
             ('Las preguntas frecuentes', 'Excursiones → la excursión → caja «Preguntas frecuentes», debajo del formulario', 'Al final de la página de la excursión y en Google'),
             ('Una excursión nueva', 'Excursiones → «Añadir nueva excursión»', 'Una página nueva y una tarjeta más en Experiences'),
             ('El orden de las tarjetas', 'La caja «Orden en la web», a la derecha de cada excursión', 'En Experiences: el 1 sale primero'),
             ('Las excursiones del pie', 'Pestaña «Tarjeta» → «Destacar en el pie de la web»', 'En el pie de todas las páginas'),
             ('Un paquete VIP', 'Paquetes → el paquete, o «Añadir nuevo paquete»', 'Su capítulo en VIP Packages y en el pie'),
             ('Las fotos de la portada', 'Galería → «Home gallery»', 'En «Straight from the trip», en la portada'),
             ('El WhatsApp de los botones', 'Panel → «Número de WhatsApp para reservas»', 'En todos los botones de reservar de excursiones, paquetes y galería'),
         ],
         caja=dict(titulo='Lo que lleva Postsicionate',
                   texto='El diseño, la cabecera con el botón «Book Now», el pie, el resto de la portada y las páginas Transfers, Your Host, Contact y Executive Protection. Para cambiar algo de ahí, escríbanos.',
                   notas=[('Siempre a salvo', 'Cada vez que guarda, la versión anterior queda guardada. Todo se puede deshacer.'),
                          ('En inglés', 'El formulario le habla en español; lo que leen sus clientes se escribe en inglés.')])),

    dict(tipo='principios', acento='oro', antetitulo='Nueve costumbres',
         titulo='Lo que hace fácil cada cambio',
         items=[
             ('oro', 'Escriba en inglés',
              'Sus clientes leen en inglés, como toda la web. Las etiquetas del formulario están en español solo para usted.'),
             ('noche', 'Guarde con «Actualizar»',
              'El botón azul, arriba a la derecha. En unos segundos el cambio está en la web; si no lo ve, recargue la página.'),
             ('bronce', 'Borrador para retirar',
              'Para quitar algo de la web, cambie su estado a Borrador. Se queda guardado tal cual y vuelve con «Publicar» cuando usted quiera.'),
             ('oro', 'Todo se puede deshacer',
              '«Revisiones» guarda cada versión. Con «Restaurar esta revisión» vuelven los textos, el precio y las fotos de ese momento.'),
             ('noche', 'Fotos suyas y limpias',
              'Reales, nítidas y horizontales, de 1200 px de ancho o más. Sin logos ni nombres de otros operadores ni iconos de Instagram.'),
             ('bronce', 'Mírelo en el teléfono',
              'La mayoría de sus clientes ve la web en el móvil. Después de guardar, ábrala en el suyo.'),
             ('oro', 'Una palabra en dorado',
              'Donde la ayuda lo indica, una palabra entre asteriscos sale en cursiva dorada: escriba Luxury Yacht *Celebration* y «Celebration» sale en oro. Una por título.'),
             ('noche', 'Precios con «US$»',
              'Siempre igual en toda la web: US$90, y con coma en los miles: US$3,000.'),
             ('bronce', 'Cada campo le guía',
              'Debajo de cada campo hay una ayuda con ejemplos, y cada texto tiene su largo máximo para que el diseño luzca siempre igual.'),
         ],
         mapa=dict(etiqueta='Su menú', titulo='Seis entradas, a la izquierda',
                   nota='Al entrar llega directo a «Panel». En el teléfono, el menú se abre con el botón de tres rayas, arriba a la izquierda.',
                   leyenda=False,
                   arbol=[('Panel', True, 'el WhatsApp de los botones'), ('Excursiones', True, 'las quince de Experiences'),
                          ('Paquetes', True, 'los capítulos de VIP Packages'), ('Galería', True, 'las fotos de la portada'),
                          ('Medios', True, 'todas sus fotos y vídeos'), ('Perfil', True, 'su contraseña')]),
         movil='img/movil-panel.png', acento_movil='oro',
         pie_movil='<b>También en el teléfono.</b> El mismo panel, para cambios rápidos como un precio. Para una excursión nueva, mejor el ordenador.'),

    dict(tipo='pasos', acento='oro', antetitulo='Para empezar', titulo='Entrar en su panel',
         entrada='Su panel está en kingblacktour.com/wp-admin, en el ordenador o en el teléfono. La pantalla de entrada está en inglés; una vez dentro, todo le habla en español.',
         capturas=[
             dict(src='img/entrar.png', ancho=33, pie='<b>La entrada,</b> en inglés.',
                  marcas=[(88, 47.5, 1), (88, 65.5, 2), (91, 78, 3), (66, 96, 4)]),
             dict(src='img/panel-inicio.png', ancho=63, pie='<b>Su panel,</b> en español. Llega aquí al entrar.',
                  marcas=[(13.5, 40, 5), (58.5, 60, 6), (37.5, 88.5, 6)]),
         ],
         pasos=[
             ('«Username or Email Address»', 'Su usuario o su correo electrónico.'),
             ('«Password»', 'Su contraseña. Solo la conoce usted.'),
             ('«Log In»', 'Entrar. Si el ordenador es suyo, marque antes «Remember Me» y no tendrá que escribirla cada vez.'),
             ('«Lost your password?»', 'Si la olvida, escriba ahí su correo: le llega un enlace para crear una nueva.'),
             ('El menú', 'Panel, Excursiones, Paquetes, Galería, Medios y Perfil. Cada entrada se explica en las hojas siguientes.'),
             ('El WhatsApp de reservas', 'El número que reciben todos los botones de reservar. Si cambia de número, escríbalo con el 1 delante y sin espacios, y pulse «Guardar cambios».'),
         ],
         nota=('Su cuenta', 'Para cambiar la contraseña: Perfil → «Establecer nueva contraseña» → «Actualizar perfil». Para salir: su nombre, arriba a la derecha → «Cerrar sesión».')),

    dict(tipo='pasos', acento='oro', antetitulo='Excursiones', titulo='Cambiar una excursión',
         entrada='En Excursiones, pulse el nombre de la que quiere cambiar. Cada pestaña del formulario es un trozo de su página: cambie lo que haga falta y guarde con «Actualizar».',
         capturas=[
             dict(src='img/excursion-arriba.png', ancho=100,
                  marcas=[(70, 19.2, 1), (64, 56, 2), (92, 34.2, 3), (90, 45.2, 4), (87, 67, 5), (84, 91.2, 6)]),
         ],
         pasos=[
             ('El nombre', 'En inglés. Es el título de su página y de su tarjeta.'),
             ('Las siete pestañas', 'Tarjeta, Portada, Cómo es el día, Qué incluye, Fotos y vídeos, Llamadas a reservar y Antes de reservar. La hoja 7 muestra qué llena cada una.'),
             ('Estado', 'Para retirarla de la web: «Editar» → Borrador → «Aceptar» → «Actualizar». Para volver a ponerla, «Publicar».'),
             ('Revisiones', '«Explorar» enseña cada versión guardada; «Restaurar esta revisión» devuelve la que usted elija.'),
             ('Actualizar', 'Guarda y publica el cambio en la web.'),
             ('Orden en la web', 'El lugar de su tarjeta en Experiences: el 1 sale primero. Si mete una en medio, súbale un número a las que van detrás.'),
         ],
         nota=('Preguntas frecuentes', 'Van en su propia caja, debajo del formulario: entre cuatro y diez, con su respuesta, en inglés. Salen al final de la página y también en Google.')),

    dict(tipo='pasos', acento='oro', antetitulo='Excursiones · Pestaña «Tarjeta»', titulo='El precio y la tarjeta',
         entrada='La pestaña «Tarjeta» decide cómo se ve la excursión en Experiences y en las recomendaciones de otras excursiones. El precio que escriba aquí sale en todas partes a la vez.',
         capturas=[
             dict(src='img/excursion-precio.png', ancho=58, pie='<b>En su panel,</b> la pestaña «Tarjeta».',
                  marcas=[(50, 24.5, 1), (93, 24.5, 2), (44, 56, 3), (44, 95, 4)]),
             dict(src='img/web-tarjeta.jpg', ancho=37, marco='web', pie='<b>En la web,</b> su tarjeta en Experiences.',
                  marcas=[(56, 7.8, 5), (91, 30, 6), (91, 60.5, 6), (91, 77.5, 7), (41, 92, 1)]),
         ],
         pasos=[
             ('Precio', 'Con «US$» delante y coma en los miles: US$90, US$3,000.'),
             ('Por', 'per person, per group… Sale junto al precio.'),
             ('Precio «desde»', 'Marcado, la tarjeta dice «From US$90». Desmarcado, para las privadas: «US$3,000 per group».'),
             ('Destacar en el pie', 'Las marcadas salen en la columna «Experiences» del pie de todas las páginas. Cinco quedan bien.'),
             ('Etiqueta sobre la foto', 'Dos o tres palabras: On the water, Adrenaline, Nightlife. Los botones de filtro de Experiences se marcan aparte, en «Filtros donde aparece».'),
             ('Foto, título y resumen', 'Una foto horizontal de 1200 px o más y una frase que invite.'),
             ('Dos datos cortos', 'Debajo del resumen: Full day, Adults only.'),
         ]),

    dict(tipo='pagina', n='7', acento='oro', antetitulo='Excursiones · Una excursión nueva',
         nombre='Pestaña por pestaña', url='Así se ve la página de Saona Island, con lo que llena cada pestaña.',
         pregunta='¿Dónde sale en la web lo que escribo en cada pestaña?',
         titulo_logica='Las siete pestañas',
         tira='img/strip-saona.jpg', alto_tira=2104, ancho_tira=176,
         marcas=[None, 60, 733, 1450, 2050, 2587, 3672],
         logica=[
             ('Tarjeta', 'Su tarjeta en Experiences y en las recomendaciones (hoja anterior).'),
             ('Portada', 'La primera pantalla: foto de fondo, lugar, tipo de salida, título, dos o tres frases y el mensaje de WhatsApp.'),
             ('Cómo es el día', 'De dos a ocho momentos, en orden. Cuatro quedan muy bien.'),
             ('Qué incluye', 'Una cosa por línea, y una nota debajo si hace falta.'),
             ('Fotos y vídeos', 'La galería, que se abre a pantalla completa, y hasta cuatro vídeos verticales.'),
             ('Llamadas a reservar', 'Las frases junto a los botones de WhatsApp y el cierre de la página.'),
             ('Antes de reservar', 'Notas prácticas (edad, qué llevar, horario) y hasta cuatro excursiones para recomendar.'),
         ],
         nota=('Para crearla', 'Excursiones → «Añadir nueva excursión» → el nombre en inglés → las siete pestañas → «Publicar». Si falta algo obligatorio, queda en borrador y un aviso le dice qué falta.'),
         lista=dict(titulo='Antes de empezar, tenga a mano', nota='Marque al tenerlo',
                    grupos=[('Para publicar', 'lo que pide el formulario', 'need',
                             ['El nombre en inglés y el precio.',
                              'Una foto horizontal para la tarjeta (1200 px o más) y otra para la portada (1600 px o más).',
                              'Lo que incluye y de dos a ocho momentos del día, en orden.']),
                            ('Para que luzca', 'la hará más fuerte', 'rec',
                             ['Cuatro fotos o más para la galería, vídeos verticales si los tiene, y de cuatro a diez preguntas frecuentes.'])]),
         pie_tira='<b>La página completa, vista en ordenador.</b> Cada número es una pestaña. La 1, la tarjeta, sale en Experiences.'),

    dict(tipo='pagina', n='3', acento='oro', antetitulo='Paquetes',
         nombre='Un paquete VIP', url='Así se ve el capítulo de Luxury Yacht Celebration en VIP Packages.',
         pregunta='¿Dónde sale cada parte de un paquete?',
         titulo_logica='Las tres pestañas, en la página',
         tira='img/strip-paquete.jpg', alto_tira=667, ancho_tira=290,
         marcas=[None, 137, 385, 1001, 1750, (1330, 86)],
         logica=[
             ('Línea del índice', 'Pestaña «Presentación»: la frase corta que sale junto al nombre, en el índice de arriba de VIP Packages.'),
             ('Nombre y presentación', 'El antetítulo, el nombre con su palabra dorada entre asteriscos (Luxury Yacht *Celebration*) y dos o tres frases.'),
             ('Las cinco fotos', 'Exactamente cinco, con un pie corto. La primera es la grande; todas se abren a pantalla completa.'),
             ('El recorrido', 'Pestaña «El recorrido»: de dos a ocho momentos, con hora si la tiene.'),
             ('Lo que incluye además', 'La lista de extras y una nota, por ejemplo el depósito.'),
             ('Precio y reserva', 'Pestaña «Precio y reserva»: la tarjeta dorada con el precio, «Por», hasta seis datos y el mensaje de WhatsApp.'),
         ],
         nota=('Añadir o retirar', 'Paquetes → «Añadir nuevo paquete» → las tres pestañas → «Publicar». «Orden en la web» decide su lugar. Para retirarlo, Estado → Borrador. Cada paquete publicado sale solo en el pie; si su nombre es largo, escriba uno corto en «Nombre en el pie de la web».'),
         lista=dict(titulo='Antes de empezar, tenga a mano', nota='Marque al tenerlo',
                    grupos=[('Para publicar', 'lo que pide el formulario', 'need',
                             ['Cinco fotos del paquete, con un pie corto para cada una.',
                              'El precio y para quién es: per person, o per group · up to 17 guests.',
                              'De dos a ocho momentos, en orden, y el mensaje que quiere recibir por WhatsApp.'])]),
         pie_tira='<b>Un capítulo de VIP Packages, en ordenador.</b> Los números señalan cada parte; la 1 está en el índice de arriba de la página.'),

    dict(tipo='pasos', acento='oro', antetitulo='Galería', titulo='Las fotos de la portada',
         entrada='La sección «Straight from the trip» de la portada sale de Galería → «Home gallery». Ocho fotos forman el mosaico; al tocar cualquiera se abren todas a pantalla completa, con dos tarjetas que invitan a escribirle por WhatsApp.',
         capturas=[
             dict(src='img/galeria-fotos.png', ancho=56, pie='<b>En su panel,</b> Galería → «Home gallery», pestaña «Las fotos».',
                  marcas=GALERIA_MARCAS),
             dict(src='img/web-galeria.jpg', ancho=40, marco='web', pie='<b>En la portada,</b> el mosaico de ocho.',
                  marcas=[(5, 27, 2), (53.5, 27, 3), (77, 77, 4)]),
         ],
         lado=True, ancho_lado=250,
         capturas_lado=[
             dict(src='img/web-tarjeta-wa.png', marco='web', pie='<b>Dentro de la galería,</b> la tarjeta tras la foto 15.',
                  marcas=[(84, 22, 5)]),
         ],
         pasos=[
             ('Abrir la galería', 'Galería → «Home gallery». Es la única, la de la portada.'),
             ('Ordenar', 'Pestaña «Las fotos»: las flechas ← → mueven cada foto. Las ocho primeras forman el mosaico; la primera es la grande.'),
             ('La segunda, vertical', 'Va en la casilla alta del mosaico, así que una foto vertical luce más.'),
             ('Añadir o quitar', '«Añadir fotos», al final de la lista, abre su biblioteca. La × quita una foto de la galería, y la foto sigue en Medios. De 8 a 80 fotos; la octava del mosaico lleva encima el total.'),
             ('Las tarjetas de WhatsApp', 'Última pestaña: tras qué foto sale la del medio (hoy, tras la 15), sus textos y el mensaje que le llega.'),
             ('Actualizar', 'Y mírelo en la portada, en el teléfono.'),
         ]),

    dict(tipo='pasos', acento='oro', antetitulo='Medios', titulo='Subir y describir sus fotos',
         entrada='Todas sus fotos y vídeos viven en Medios. Desde cualquier campo de foto del formulario, «Elegir foto» o «Añadir fotos» abre esta misma biblioteca, donde también puede subir fotos nuevas.',
         capturas=[
             dict(src='img/medios-lista.png', ancho=100, pie='<b>Medios,</b> su biblioteca.',
                  marcas=[(48.5, 20.5, 1)]),
         ],
         lado=True, ancho_lado=270,
         capturas_lado=[
             dict(src='img/medios-alt.png', pie='<b>Al abrir una foto,</b> su descripción.',
                  marcas=[(93, 53, 3)]),
         ],
         pasos=[
             ('Subir', 'Medios → «Añadir medios» → arrastre las fotos al recuadro o pulse «Seleccionar archivos».'),
             ('O desde el formulario', '«Elegir foto» → pestaña «Subir archivos». La foto queda subida y elegida a la vez.'),
             ('Describirla', 'Pulse la foto y escriba en «Texto alternativo» qué se ve, en inglés. Por ejemplo: Five friends walking on the sand carrying pineapples. Lo leen Google y las personas que usan lector de pantalla.'),
             ('El encuadre en el teléfono', 'Si la portada de una excursión corta una cara en el móvil, cambie «Encuadre en el teléfono»: 50% 50% es el centro y 70% 50% lleva el foco a la derecha.'),
         ],
         nota=('Su biblioteca', 'En Medios las fotos se quedan. Si una deja de servir, quítela de la excursión o de la galería: la biblioteca la conserva por si vuelve a hacer falta.')),

    dict(tipo='revision', acento='oro', antetitulo='Para tenerla a mano', titulo='Cualquier cambio, en seis pasos',
         pasos=[
             ('oro', 'Entre en su panel', 'kingblacktour.com/wp-admin, con su usuario y su contraseña.'),
             ('noche', 'Elija qué cambiar', 'Excursiones, Paquetes o Galería, en el menú de la izquierda.'),
             ('bronce', 'Abra la ficha', 'Pulse su nombre en la lista.'),
             ('oro', 'Cambie el campo', 'En inglés lo que leen sus clientes. Debajo de cada campo hay una ayuda con ejemplos.'),
             ('noche', 'Pulse «Actualizar»', 'Arriba a la derecha. Una ficha nueva se publica con «Publicar».'),
             ('bronce', 'Mírelo en el teléfono', 'Abra la página en su móvil; si no ve el cambio, recárguela.'),
         ],
         cajas=[('oro', 'Lo que hace usted', 'Sus excursiones, sus paquetes, las fotos de la portada y el WhatsApp de reservas: precios, textos, fotos, orden, y qué se publica y qué no.'),
                ('noche', 'Lo que hacemos nosotros', 'El diseño, la cabecera, el pie y las demás páginas. Escríbanos también si algo se ve extraño, sobre todo en el teléfono, o si no puede entrar.')],
         lineas_notas=0,
         firma='Su web, al día y con su estilo, desde su propio panel.'),
]

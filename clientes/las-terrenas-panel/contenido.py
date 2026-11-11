# -*- coding: utf-8 -*-
# Las Terrenas Transfers & Tours · Guía rápida del panel para Joana (edición de entrega).
# Las capturas están hechas con la sesión de Joana, para que el menú sea el suyo y no el
# de administrador. Los nombres y correos de clientes van difuminados a propósito.

CLIENTE = dict(
    nombre='Las Terrenas Transfers & Tours',
    cabecera='Guía rápida de su panel',
    pie='Guía de uso · Noviembre de 2026',
    fecha='Noviembre de 2026',
    logo='img/lt-logo.png',
    para='Joana', cargo='Excelia Dominican Tours',
    quien='usted',
    pregunta='¿Cómo mantengo mi web al día yo misma?',
    palabra_pintada='yo misma',
    etiqueta_pregunta='La pregunta que responde esta hoja',
    archivo='guia-panel-las-terrenas-joana', version='1.2',
    asunto='Guía rápida del panel de lasterrenas-bestexcursions.com',
)

MARCA = dict(
    tinta='#073E62', texto='#2A3B49', gris='#55636F', linea='#DFDBCF', papel='#F6F5F0',
    acentos={
        'rojo':  ('#E46C48', '#C14A28'),   # coral
        'azul':  ('#1C7FC4', '#0B5580'),   # caribe
        'verde': ('#0C9060', '#087049'),   # samaná
        'sol':   ('#E4A824', '#8A6410'),   # ámbar
    },
    tricolor=['azul', 'verde', 'sol'], pincel='sol',
    necesario='#C14A28', recomendado='#0B5580', ok='#0C9060', ok_d='#087049', falta='#E46C48',
)

HOJAS = [

    # ---- 01 Portada -----------------------------------------------------
    dict(tipo='portada', acento='sol',
         etiqueta='La pregunta que responde esta guía',
         titulo='Guía rápida de su panel',
         subtitulo='Lo que usted puede cambiar en lasterrenas-bestexcursions.com: dónde se hace, cómo se hace y dónde aparece en la web.',
         escritorio='img/panel-contacto.jpg', movil='img/movil-panel.png'),

    # ---- 02 El panel de un vistazo --------------------------------------
    dict(tipo='intro', acento='azul', antetitulo='Su panel de un vistazo',
         titulo='Usted escribe, la web lo publica',
         entrada='Su panel es un formulario. Usted rellena los datos de cada excursión y sus datos de contacto, y en unos segundos la web los publica con su diseño de siempre. Esta tabla le dice dónde se cambia cada cosa y dónde la ven sus clientes.',
         columnas=['Lo que quiere cambiar', 'Dónde se hace, en su panel', 'Dónde se ve en la web'],
         anchos=[29, 38, 33], marcas_columnas=False,
         filas=[
             ('El WhatsApp de los botones', 'Panel → «Contacto» → «WhatsApp principal»',
              'En el botón verde de la cabecera, en cada excursión y en el pie'),
             ('El correo donde llegan las reservas', 'Panel → «Contacto» → «Correo de reservas»',
              'En el pie y en la página de contacto'),
             ('El precio de una excursión', 'Tours → la excursión → pestaña «Price»',
              'En su tarjeta del catálogo y en su página, a la vez'),
             ('Los días que opera y la hora de salida', 'Tours → la excursión → pestaña «Operation»',
              'En la barra de datos de la ficha y en la tarjeta'),
             ('Qué incluye, qué llevar, qué no incluye', 'Tours → la excursión → pestaña «Lists»',
              'En los cuatro bloques del final de la ficha'),
             ('La foto de una excursión', 'Tours → la excursión → «Imagen destacada», en la columna de la derecha',
              'En la portada de su ficha y en su tarjeta del catálogo'),
             ('Las preguntas de una excursión', 'Tours → la excursión → caja «Preguntas frecuentes», debajo del formulario',
              'Al final de la ficha y en Google'),
             ('Retirar una excursión de la web', 'Tours → la excursión → Estado: Borrador',
              'Desaparece del catálogo sin que se pierda nada'),
         ],
         caja=dict(titulo='Lo que lleva Postsicionate',
                   texto='El diseño, la portada, los traslados, los chárters, las excursiones privadas, el alojamiento, las preguntas generales y el pie. Para cambiar algo de ahí, escríbanos.',
                   notas=[('Siempre a salvo', 'Cada vez que guarda, la versión anterior queda guardada. Todo se puede deshacer.'),
                          ('En inglés', 'El formulario le habla en español; lo que leen sus clientes se escribe en inglés.')])),

    # ---- 03 Costumbres --------------------------------------------------
    dict(tipo='principios', acento='verde', antetitulo='Nueve costumbres',
         titulo='Lo que hace fácil cada cambio',
         items=[
             ('azul', 'Escriba en inglés',
              'Sus clientes leen en inglés, como toda la web. Las etiquetas del formulario están en español solo para usted.'),
             ('verde', 'Guarde con el botón azul',
              'Arriba a la derecha. En unos segundos el cambio está en la web; si no lo ve, recargue la página.'),
             ('sol', 'Borrador para retirar',
              'Para quitar una excursión de la web, cambie su estado a Borrador. Se queda guardada tal cual y vuelve con «Publicar» cuando usted quiera.'),
             ('rojo', 'Todo se puede deshacer',
              '«Revisions», en la columna de la derecha, guarda cada versión. Con «Restaurar» vuelven los textos, el precio y las fotos de ese momento.'),
             ('azul', 'Fotos horizontales y grandes',
              'Reales y nítidas, de 1200 px de ancho o más. La web genera sola los tamaños pequeños; usted sube el archivo más grande que tenga.'),
             ('verde', 'Mírelo en el teléfono',
              'La mayoría de sus clientes ve la web en el móvil. Después de guardar, ábrala en el suyo.'),
             ('sol', 'El precio, solo el número',
              'El «US$» ya está puesto delante del campo. Escriba 95, no US$95.'),
             ('rojo', 'Las solicitudes se marcan',
              'Cada reserva nace como «Nueva». Al atenderla, póngala en Confirmada, Cerrada o Cancelada: así la pantalla le dice de un vistazo qué le falta por hacer.'),
             ('azul', 'Cada campo le guía',
              'Debajo de cada casilla hay una línea que explica qué escribir y en qué parte de la web aparece.'),
         ],
         mapa=dict(etiqueta='Su menú', titulo='Seis entradas, a la izquierda',
                   nota='Al entrar llega directa al Panel, sin pasar por ninguna pantalla de WordPress. En el teléfono, el menú se abre con el botón de tres rayas, arriba a la izquierda.',
                   leyenda=False,
                   arbol=[('Panel', True, 'sus datos de contacto y los avisos'),
                          ('Media', True, 'todas sus fotos y vídeos'),
                          ('Tours', True, 'las catorce excursiones'),
                          ('Mensajes', True, 'lo que llega del formulario de contacto'),
                          ('Reservas', True, 'las solicitudes de excursión'),
                          ('Profile', True, 'su contraseña')]),
         movil='img/movil-panel.png', acento_movil='verde',
         pie_movil='<b>También en el teléfono.</b> El mismo panel, para cambios rápidos como un precio. Para una excursión nueva, mejor el ordenador.'),

    # ---- 04 Entrar ------------------------------------------------------
    dict(tipo='pasos', acento='azul', antetitulo='Para empezar', titulo='Entrar en su panel',
         entrada='Su panel está en lasterrenas-bestexcursions.com/wp-admin, en el ordenador o en el teléfono. Reconocerá la pantalla por su logo. Está en inglés; una vez dentro, todo le habla en español.',
         capturas=[
             dict(src='img/entrada.jpg', ancho=42, pie='<b>La entrada,</b> con el logo de su web.',
                  marcas=[(66, 24, 1), (66, 34, 2), (62, 42, 3), (41, 52, 4)]),
             dict(src='img/panel-contacto.jpg', ancho=55, pie='<b>Su panel,</b> en español. Llega aquí al entrar.',
                  marcas=[(8, 20, 5), (29, 32, 6), (39, 52, 7)]),
         ],
         pasos=[
             ('«Username or Email Address»', 'Su usuario o su correo electrónico.'),
             ('«Password»', 'Su contraseña. Solo la conoce usted.'),
             ('«Log In»', 'Entrar. Si el ordenador es suyo, marque antes «Remember Me» y no tendrá que escribirla cada vez.'),
             ('«Lost your password?»', 'Si la olvida, escriba ahí su correo: le llega un enlace para crear una nueva.'),
             ('El menú', 'Sus seis entradas. Cada una se explica en las hojas siguientes.'),
             ('Las cuatro pestañas del Panel', 'Contacto, Precios, Aviso y Políticas.'),
             ('Las casillas', 'Debajo de cada una, una línea le dice en qué parte de la web aparece.'),
         ],
         nota=('Su cuenta', 'Para cambiar la contraseña: Profile → «Set New Password» → «Update Profile». Para salir: su nombre, arriba a la derecha → «Log Out».')),

    # ---- 05 El Panel · Contacto -----------------------------------------
    dict(tipo='pasos', acento='verde', antetitulo='Panel · Contacto', titulo='Sus datos de contacto',
         entrada='Son los datos por los que entra una reserva, así que viven en un solo sitio y desde ahí se reparten. Cambiarlos aquí los cambia en la cabecera, en el pie y en las catorce excursiones a la vez.',
         capturas=[
             dict(src='img/panel-contacto.jpg', ancho=88,
                  marcas=[(39, 52, 1), (76, 52, 2), (39, 72, 3), (39, 89, 4), (76, 89, 5)]),
         ],
         pasos=[
             ('WhatsApp principal', 'Solo números, con el código del país y sin espacios ni signos: 18492575577. Abre el botón verde de la cabecera, el de cada excursión y el del pie.'),
             ('WhatsApp alternativo', 'Con el mismo formato. Se reserva para un segundo teléfono de reservas.'),
             ('Teléfono principal', 'Tal como quiere que se lea, con espacios: +1 849 257 5577. Aparece en el pie y en la tarjeta de contacto de cada excursión.'),
             ('Correo de reservas', 'La dirección a la que llegan los mensajes del formulario. Aparece también en el pie y en contacto.'),
             ('Horario de atención', 'Una línea corta, en inglés. Aparece junto a los datos de contacto.'),
         ],
         nota=('Las casillas con asterisco', 'WhatsApp principal y Correo de reservas son las dos que la web necesita sí o sí. Las demás puede dejarlas vacías.')),

    # ---- 06 El Panel · Precios, aviso y políticas -----------------------
    dict(tipo='pasos', acento='sol', antetitulo='Panel · Precios y políticas', titulo='Las otras dos pestañas',
         entrada='Lo que se toca pocas veces, y justo por eso conviene saber dónde está el día que haga falta: cómo se enseñan las tarifas y qué dice cada excursión sobre cancelaciones.',
         capturas=[
             dict(src='img/panel-precios.jpg', ancho=50, pie='<b>Precios.</b> Un interruptor y la moneda.',
                  marcas=[(24, 49, 1), (78, 52, 2)]),
             dict(src='img/panel-politicas.jpg', ancho=47, pie='<b>Políticas.</b> Hoy las tres están vacías.',
                  marcas=[(46, 32, 3), (57, 53, 4)]),
         ],
         pasos=[
             ('«Mostrar los precios en la web»', 'Encendido, cada excursión enseña su tarifa. Apagado, todas dicen «Price on request». Sirve para una temporada en la que los precios estén en revisión.'),
             ('Moneda', 'Tres letras. Es la moneda en la que están expresadas todas las tarifas.'),
             ('Las tres políticas de cancelación', 'Estándar, flexible y por el clima. Cada excursión tiene asignada una de las tres, en su pestaña «Booking»; hoy las catorce están en estándar.'),
             ('El recuadro que importa', 'Con las catorce en estándar, basta con escribir el primero. Los otros dos quedan de reserva para el día que una excursión necesite condiciones distintas.'),
         ],
         nota=('Lo que falta aquí', 'Los tres recuadros están vacíos, así que hoy ninguna ficha dice qué pasa si se cancela. Escriba el primero cuando pueda; nosotros nos encargamos de que aparezca en la ficha.')),

    # ---- 07 Tours · la lista --------------------------------------------
    dict(tipo='pasos', acento='azul', antetitulo='Tours', titulo='Sus catorce excursiones',
         entrada='Tours es el catálogo por dentro. Cada línea es una excursión: su página en la web y su tarjeta en el catálogo. Para cambiar cualquier cosa de una, pulse su nombre.',
         capturas=[
             dict(src='img/tours-lista.jpg', ancho=90,
                  marcas=[(27, 32, 1), (24, 14, 2), (41, 32, 3), (59, 32, 3), (89, 32, 4), (31, 9, 5)]),
         ],
         pasos=[
             ('El nombre', 'Púlselo para abrir la excursión. Es el título de su página y de su tarjeta.'),
             ('«All (14)»', 'Cuántas hay publicadas. Si alguna pasa a borrador, aparece aquí un segundo recuento.'),
             ('Destinations y Experiences', 'La zona y el tipo de día. Deciden el color de la tarjeta y en qué filtro del catálogo aparece.'),
             ('Published', 'La fecha. Pulsando «Date» se ordena la lista por antigüedad.'),
             ('«Add New Tour»', 'Para crear una excursión nueva. Antes de empezar, tenga listos el nombre, el precio y una foto horizontal grande.'),
         ],
         nota=('Si no la encuentra', 'Arriba a la derecha hay un buscador. Escriba una palabra del nombre y pulse «Search Tours».')),

    # ---- 08 La ficha · las pestañas -------------------------------------
    dict(tipo='pasos', acento='verde', antetitulo='Tours · una excursión', titulo='La ficha por dentro',
         entrada='Al abrir una excursión, lo primero que ve es el formulario «Tour details», repartido en cinco pestañas. Cada pestaña es un trozo de su página. Cambie lo que haga falta y guarde con el botón azul.',
         capturas=[
             dict(src='img/ficha-operation.jpg', ancho=52, pie='<b>Operation.</b> Cómo funciona el día.',
                  marcas=[(19, 25, 1), (36, 39, 2), (23, 76, 3), (93, 8, 4)]),
             dict(src='img/ficha-price.jpg', ancho=45, pie='<b>Price.</b> La tarifa, que sale en dos sitios.',
                  marcas=[(10, 39, 5), (10, 52, 6), (36, 77, 7), (36, 90, 8)]),
         ],
         pasos=[
             ('Tagline', 'Una línea, debajo del título, en la portada de la ficha.'),
             ('Duration y Departure times', 'Salen en la barra de datos, justo bajo la foto de portada.'),
             ('Days of operation', 'Marque los días que opera. Es lo que lee el visitante y lo que ve en la tarjeta del catálogo.'),
             ('El botón azul', 'Guarda y publica. A su lado, «View Post» abre la ficha en la web para comprobarla.'),
             ('Price from', 'Solo el número: el «US$» ya está puesto. Es el precio que sale en la tarjeta y en la caja de reserva.'),
             ('Child price', 'El precio de niños. Si la excursión no admite niños, déjelo vacío.'),
             ('Price unit', 'Por persona, por vehículo o por reserva entera.'),
             ('Price note', 'Una línea bajo el precio para las condiciones: «Children 4 to 10 · Available for weddings».'),
         ],
         nota=('Las otras tres pestañas', '«Lists» lleva lo que incluye, lo que no incluye, qué llevar y las restricciones. «Booking» lleva el mensaje de WhatsApp y la política de cancelación. «Presentation» decide el color de la tarjeta y si sale en la portada.')),

    # ---- 09 La ficha · fotos --------------------------------------------
    dict(tipo='pasos', acento='rojo', antetitulo='Tours · una excursión', titulo='Las fotos y las preguntas',
         entrada='La foto es la mitad de la decisión de un visitante. En una excursión hay dos sitios donde se ponen fotos, y conviene no confundirlos.',
         capturas=[
             dict(src='img/ficha-presentation.jpg', ancho=50, pie='<b>Presentation.</b> El color y la portada.',
                  marcas=[(86, 35, 1), (16, 39, 2), (5, 67, 3), (36, 85, 4)]),
             dict(src='img/ficha-fotos.jpg', ancho=47, pie='<b>Fotos y vídeo.</b> La galería de la ficha.',
                  marcas=[(36, 55, 5), (8, 80, 5), (36, 92, 6)]),
         ],
         pasos=[
             ('La imagen destacada', 'En la columna de la derecha, bajo el nombre de la excursión. Es la foto que hoy sale en la portada de la ficha y en la tarjeta del catálogo. Para cambiarla, púlsela y elija otra.'),
             ('Hero image y Card image', 'Dos campos para separar la foto grande de la de la tarjeta. Hoy están vacíos en casi todas las excursiones, y por eso manda la imagen destacada.'),
             ('Show on homepage', 'Encendido, la excursión aparece entre las seis de la portada.'),
             ('Card colour', 'El color de la tarjeta en el catálogo. En automático lo decide la zona: verde el interior, turquesa la bahía, azul el mar.'),
             ('Galería', 'De cuatro a ocho fotos de la excursión. Suba el archivo más grande que tenga: la web genera sola los tamaños pequeños.'),
             ('Vídeo', 'Un clip corto, subido a la biblioteca de medios. Es opcional; si no hay ninguno, la sección no aparece.'),
         ],
         nota=('Las preguntas frecuentes', 'Más abajo, en su propia caja, hasta ocho preguntas con su respuesta, en inglés. Salen al final de la ficha y Google puede mostrarlas directamente en los resultados.')),

    # ---- 10 Reservas ----------------------------------------------------
    dict(tipo='pasos', acento='sol', antetitulo='Reservas', titulo='Las solicitudes que llegan',
         entrada='Cuando alguien rellena el formulario de una excursión, la solicitud se guarda aquí antes de abrirle WhatsApp. Esa es la razón de ser de esta pantalla: si el visitante se distrae y no llega a escribirle, usted ya tiene sus datos.',
         capturas=[
             dict(src='img/reservas-lista.jpg', ancho=55, pie='<b>La lista.</b> Los nombres van tapados en esta guía.',
                  marcas=[(26, 32, 1), (48, 27, 2), (78, 32, 3), (90, 27, 4)]),
             dict(src='img/solicitud.jpg', ancho=42, pie='<b>Una solicitud</b>, por dentro.',
                  marcas=[(40, 56, 5), (40, 78, 6), (30, 94, 7), (72, 22, 3)]),
         ],
         pasos=[
             ('El código', 'LT-2026-0001 y siguientes. Púlselo para abrir la solicitud entera.'),
             ('Excursión, fecha y personas', 'Lo que pidió el visitante: qué día quiere ir y cuántos van.'),
             ('Estado', 'Nace como «Nueva». Al atenderla, elija Confirmada, Cerrada o Cancelada y pulse «Update». Así la lista le dice de un vistazo qué le queda por hacer.'),
             ('Recibida', 'Cuándo entró la solicitud. Pulsando la columna se ordena por fecha.'),
             ('Nombre, correo y WhatsApp', 'Lo que dejó el visitante. El WhatsApp es obligatorio en el formulario; el correo es opcional.'),
             ('Importe y estado del precio', '«Se confirma al responder»: la web no cierra un precio, lo acuerda usted en la conversación.'),
             ('«Responder por WhatsApp»', 'Abre el chat con esa persona, con el código de la solicitud ya escrito.'),
         ],
         nota=('Lo primero que conviene hacer', 'Hay seis solicitudes esperando, la más antigua del 14 de octubre. Repáselas y marque el estado de las que ya atendió: a partir de ahí, la pantalla empieza a trabajar para usted.')),

    # ---- 11 Mensajes, Medios y Perfil -----------------------------------
    dict(tipo='pasos', acento='azul', antetitulo='Mensajes, Media y Profile', titulo='Las tres últimas entradas',
         entrada='Las tres se usan poco, pero conviene saber qué hay en cada una. Mensajes es el otro buzón, Media es su almacén de fotos y Profile es su cuenta.',
         capturas=[
             dict(src='img/mensajes.jpg', ancho=34, pie='<b>Mensajes.</b> El formulario de contacto.',
                  marcas=[(26, 32, 1)]),
             dict(src='img/medios.jpg', ancho=32, pie='<b>Media.</b> Sus fotos y vídeos.',
                  marcas=[(40, 9, 2)]),
             dict(src='img/perfil-clave.jpg', ancho=32, pie='<b>Profile.</b> Su contraseña.',
                  marcas=[(49, 46, 3), (51, 55, 4)]),
         ],
         pasos=[
             ('Mensajes', 'Lo que llega por el formulario de la página de contacto, que es distinto del de las excursiones. Hoy hay dos.'),
             ('«Add Media File»', 'Para subir fotos y vídeos sin pasar por una excursión. Todo lo que suba queda aquí y se puede reutilizar.'),
             ('«Set New Password»', 'Crea una contraseña nueva. Después, «Update Profile» al final de la página.'),
             ('«Log Out Everywhere Else»', 'Cierra su sesión en los demás aparatos. Útil si entró desde un ordenador que no es suyo.'),
         ],
         nota=('Si algo no le cuadra', 'Escríbanos y lo miramos. Nada de lo que haga aquí es irreversible: cada excursión guarda sus versiones anteriores y se pueden recuperar.')),
]

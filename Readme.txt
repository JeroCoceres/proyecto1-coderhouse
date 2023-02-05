La pagina web fue diseñada individualmente por el alumno de CoderHouse Jeronimo Coceres Liubici, utilizando Python, Django y plantillas de Bootstrap.
Me propuse crear una pagina web que, en caso de ser exitosa, pueda ser obsequiada al refugio de animales de mi ciudad natal, un pueblo de 100.000 habitantes.

La misma emula una web de un refugio de animales, donde se muestran listas de los animales agregados, dividiendolos en Perros, Gatos y Otros. Todos como diferentes objetos(modelos)
dentro de una misma aplicación.

Desde la nav bar tenemos 4 opciones. 
1-La pagina de inicio, con información y presentación
2-Una pagina no desarrollada aún, donde me gustaría agregar un enlace de mercadopago para realizar donaciones.
3-Un menú desplegable donde se da acceso a cada categoría de animal (Perros, Gatos y Otros).
4-Una pagina llamada "Quienes somos" donde se muestra información del personal que trabaja en dicho refugio.
5-Una pagina llamada "Acerca de mi" con información adicional.

Punto 3:

El punto 3 será un sitio donde podamos acceder a cada categoría de animal (cada una con un html distinto) desde donde ver (mediante un bucle for) los animales cargados.
Cada animal tendrá la siguiente información:    Nombre (mediante un CharField)
								Vacunación (mediante un BoolField)
								Castrado (mediante un BoolField)


Desde cada html de cada categoría (Perros, Gatos u Otros), habrá un boton que permitirá cargar un nuevo elemento. Este boton agregará el elemento y mostrará un cartel de elemento creado. Se podrán editar y borrar los elementos (siempre y cuando el usuario este autenticado como superuser)

Dentro de el html de cada categoría encontraremos en la navbar, el buscador. El mismo buscará elementos de cada categoría (ejemplo el buscador desde perros solo mostrara perros que contengan esas palabras)

Tenemos el apartado miembros donde podemos encontrar información de los integrantes de la organización, con igual funcionamiento al de los animales.

Tuve dos problemas que no pude resolver. 
1ro: hice todo lo explicado en clase para subir una imagen como avatar, pero al realizarlo la imagen no se guardaba (a menos que lo hiciera desde el panel de admin), por ende no puse la imagen modificable por el superuser desde index (como requería el trabajo final).
2do: Tuve un error que tampoco pude solucionar, al tratar de modificar los datos de usuario (no el perfil) como ser Nombre y Apellido. Me aparecía este error:
"UNIQUE constraint failed: auth_user.username". En el video se muestra.

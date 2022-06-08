Mapa del sitio:

Sidebar tiene los accesos a las distintas urls de la aplicacion

Home -- http://127.0.0.1:8000
Es un landing page que permite navegar

Crear Usuario -- http://127.0.0.1:8000/crearusuario
Formulario para crear User propios de Django que permite tambien elegir el grupo al que pertenecera ese User

Ver Tickets -- http://127.0.0.1:8000/tickets
Muestra al admin todos los tickets generados permitiendo cerrarlo con un comentario de "solucion"

Ver Usuarios en Tabla -- http://127.0.0.1:8000/mostrarusuarios
Muestra los usuarios creados en una tabla con css y bootstrap


ABP2:

Para la revision de la actividad pueden revisar en el archivo settings.py del proyecto que la conexion con la base de datos es a traves de my sql, se realizo la migracion a traves de dumpdata y loaddata del .json respectivo. Por otra parte la aplicacion no realiza explicitamente lo solicitado respecto a comentarios y su CRUD ya que antes de realizar los ABP del modulo estaba avanzando en el proyecto principal pero si se pueden generar tickets y cerrarlos en el apartado de "Ver Tickets" al loguear con el usuario administrador entregado mas abajo. Por otra parte el proyecto no incluye la eliminacion de lso tickets ya que las reglas del negocio no lo permiten pero si vi en los videos como realizarlo

/admin

El login esta en el navbar superior en el enlace de "Login"

Username: admin
Password: admin

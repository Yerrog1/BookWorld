# BookWorld

Mi proyecto en Django es una tienda de libros en la que el cliente elige los libros que quiere comprar, rellena sus
datos y le llegara una factura al correo anteriormente especificado.
Para añadir libros o autores a la base de datos se hace desde la ventana de Admin, que ha sido levemente configurada
para hacer más cómoda la inserción de nuevos libros.
Para acceder a la ventana de Admin se debe ir a la url /admin y loguearse con las credenciales que se muestran a
continuación.
No olvidar instalar las dependencias con pip install -r requirements.txt

### Credenciales Admin:

- User: user
- Password: abc1234.

### Posibles mejoras:

- Añadir una gestión de usuarios mejor, en la que un cliente pueda iniciar sesión, comprar, ver sus pedidos, ...
- Mejorar la adaptación a diferentes resoluciones.
- Implementar por completo la gestión de imágenes. Está empezada, pero no se deben gestionar como están ahora mismo para
  no sobrecargar la base de datos.
- Añadir métodos de pago al hacer un pedido.

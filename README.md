## Parametros 
Los parametros de configuracion disponibles para este proyecto son:

host:       (str) Indica la direccion del servidor
port:       (int) Indica el puerto del servidor
use_log:    (bool) Indica si el programa debe guardas los logs del servidor
debug:      (bool) Indica si los logs deben imprimirse en pantalla
log_folder: (str) Indica el folder donde los logs seran almacenados
log_file:   (str) Indica el nombre de del archivo que contiene los logs

Obs: Por ahora debug solo hace sentido si use_log es true

## Archivos 
client.py contiene el cliente para hacer pruebas, se puede mandar mensajes al servidor y este debera contestar con el mismo mensaje en mayusculas, para cerrar la conexion mandar DESCONEXION.

parameters.yaml contiene los parametros de configuracion descritos en la version anterior.

requeriments.txt contiene los requerimientos para que el proyecto funcione correctamente.


server.py contiene el codigo del servidor.

utils.py continen funciones auxiliares

## Uso

Para probar este proyecto es necesario
1. seleccionar un puerto que no este en uso, por ejemplo el 5000 de nuestro localhost.
2. En una terminal ejecutar el servidor con $ python3 server.py 
3. En una terminal independiente a la usada en el paso 1. ejecutar el cliente con python3 client.py



RadioStream
==========
Funcionamiento del programa es el siguiente. 
Usa el fichero emisoras.xml, que contiene todas las emisoras españa de streaming en el formato xml. 
El formato es <id> <nombre><frequencia><url>.
Para que VLC funcione en modo root hay que editar el fichero bin, con un editor hexadecimal.
·sudo apt-get install hexedit
·hexedit /usr/bin/vlc

Buscar una cadena donde pone geteuid y cambiarlo por getppid, de esta manera se podra ejecutar el VLC en modo root.


stream.py 
-------------
Programa necesario para escuchar emisoras stream por la raspberry

emisoras.xml 
-----------------
Fichero de configuracion de emisoras.

LCD.py
------
Fichero donde contiene todas las funciones necesarias para mostrar la informacion por el LCD 16x2


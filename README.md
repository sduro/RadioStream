RadioStream
==========
Funcionamiento del programa es el siguiente. 
Usa el fichero emisoras.xml, que contiene todas las emisoras españa de streaming en el formato xml. 
Para el funcionamiento de la radio:
'''shell
sudo python stream.py
'''
En el codigo fuente, hay comentarios para poder usar la rádio en la plataforma x86 (pc) además de la raspberry (ARM).


Configuración
-------------
El programa requiere ejecutarse en modo root hay que cambiar un parametro del vlc binario, a continuación se describe el procedimiento de cambio.
Para que VLC funcione en modo root hay que editar el fichero bin, con un editor hexadecimal.
*sudo apt-get install hexedit
*hexedit /usr/bin/vlc
Buscar una cadena donde pone geteuid y cambiarlo por getppid, de esta manera se podra ejecutar el VLC en modo root.

emisoras.xml 
-----------------
Fichero de configuracion de emisoras. En este fichero se puedn añadir o quitar las distintas emisoras de radio siguiendo la correcta configuración.
por ejemplo:
````xml
<emisora id="1" freq="90.10" name="RNE 1" url="http://radiolive.rtve.es/rne.m3u"/>
````

Primer ejemplo de RaspberryPI + Servidor
----------------------------------------
[FormatFactoryIMG_20150312_21484.jpg](https://photos.app.goo.gl/2HWkJDmE3DCK6jaM6)
<img src="https://bitbucket.org/repo/Knp4Bg/images/1707184735-FormatFactoryIMG_20150312_21484.jpg">




-No mostrar el texto de ejecucion en consola
p = subprocess.Popen(['cvlc','--aout','alsa','-d', url,'>','/dev/null'], stdout=subprocess.PIPE) # no funciona
-usar el mismo botos de play/pausa


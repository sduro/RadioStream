#################################################################################################
#Extraccion de datos stream: http://www.listenlive.eu/spain.html
#descripcion:    Programa de radio streaming para Raspberry con lcd 16x2 usando GPIO. 
#                Esta emisora sirve para raspberry como para arquitectura X86 haciendo las
#                modificaciones pertinentes con las librerias para evitar errores de compilacion
#developer:      sergiduro@gmail.com
#Inicio:         16/02/2015
#Update:         09/01/2023
#cvlc other options:
#--volume <integer> sets the level of audio output (between 0 and 1024) 
#################################################################################################
  
import xml.etree.ElementTree as ET
import os
import subprocess, signal
import time

"""
Para la version de X86 hay que comentar los imports lcd y buttons ya
que son funciones especificas de la Raspberry y GPIO
"""
import lcd
from lcd.lcd import lcd_init, lcd_print
import buttons
from buttons.buttonsgpio import press, buttons_init

class reproductor:
    """
    Classe reproductor, play/pausa, fordward, rewind.
        getid: obtiene el numero de la emisora
        setid: pone el id de la emisora en la reproduccion
    """
    id = 1
    def __init__(self,id,items):
        self.id=id
        self.items=items
        
    def getid(self):
        """
        Devuelve el valor de la cancion
        """
        return self.id
    
    def setid(self,id):
        """
        Pone el valor de la cancion en la variable id
        """
        self.id=id
        
    def display(self):
        """
        Muestra por pantalla tanto terminal como LCD la informacion de la emisora que esta emitiendo
        """
        tree = ET.parse('emisoras.xml')
        root = tree.getroot()
        for child in root:
            if int(child.attrib['id']) == int(self.getid()):
                print child.attrib['id'],"-",child.attrib['freq'],"-",child.attrib['name'] #muestra info en terminal
                lcd_print(child.attrib['name'],child.attrib['freq']) #descomentar en version raspi /comentar en la version x86
        
    def prev(self):
        """
        Emisora anterior
        """
        if self.getid() == 1:
            self.setid(self.items)
        else:
            self.setid(self.getid() - 1)
        self.play()
        
    def next(self):
        """
        Siguiente emisora
        """
        if self.getid() == self.items:
            self.setid(1)
        else:
            self.setid(self.getid() + 1)
        self.play()
     
    def stop(self):
        """
        Para el proceso VLC si se esta ejecutando, si no es asi, reproduce el streaming
        de la emisora que corresponde segun el id cargado actual.
        """
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if 'vlc' in line:
                pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)

    def exit(self):
        """
        Funcion de salida, cierra el proceso de VLC y queda a la espera.
        """
        self.stop()
        lcd_print("RasdioStream", "Stop")
                
    def play(self):
        """
        Para el proceso VLC si se esta ejecutando, si no es asi, reproduce el streaming
        de la emisora que corresponde segun el id cargado actual.
        """
        self.stop()
        self.display()
        tree = ET.parse('emisoras.xml')
        root = tree.getroot()
        self.items = len(root)
        for child in root:
            if int(child.attrib['id']) == int(self.getid()):
                url = child.attrib['url']
                p = subprocess.Popen(['cvlc','--aout','alsa','volume','300','-d', url, '>','/dev/null'], stdout=subprocess.PIPE)
                out, err = p.communicate()
        
def main():
    """
    Programa principal con bucle infinito con lectura continua del GPIO
    """
    buttons_init()
    lcd_init()
    lcd_print("Iniciando", "Emisora")    
    tree = ET.parse('emisoras.xml')
    root = tree.getroot()
    r = reproductor(1,len(root))     
    r.play()    
    option = {1:r.play,2:r.prev,3:r.next,4:r.exit}
    try:
        while True:
            #num=int(raw_input())     #comentar para la version raspi / Descomentar esta linea para la version x86
            num=press()  #comentar esta linea para la version x86 /Descomentar para la version raspi
            if num in option:
                option[num]()
            time.sleep(0.01)
    except KeyboardInterrupt:
        GPIO.cleanup()
           
if __name__== '__main__':
    main()
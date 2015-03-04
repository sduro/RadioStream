#################################################################################################
#Extraccion de datos stream: http://www.listenlive.eu/spain.html
#descripcion:    Programa de radio streaming para Raspberry con lcd 16x2 usando GPIO. 
#                Esta emisora sirve para raspberry como para arquitectura X86 haciendo las
#                modificaciones pertinentes con las librerias para evitar errores de compilacion
#developer:      sergiduro@gmail.com
#Inicio:         16/02/2015
#################################################################################################
  
import xml.etree.ElementTree as ET
import os
import subprocess, signal
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
        return self.id
    def setid(self,id):
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
                lcd_print(child.attrib['name'],child.attrib['freq']) #descomentar en version raspi
        
    def exit(self):
        """
        Elimina el proceso del VLC
        """
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if 'vlc' in line:
                pid = int(line.split(None, 1)[0])
                print pid
                os.kill(pid, signal.SIGKILL)
        
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
        
    def play(self):
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
        self.display()
        tree = ET.parse('emisoras.xml')
        root = tree.getroot()
        self.items = len(root)
        for child in root:
            if int(child.attrib['id']) == int(self.getid()):
                url = child.attrib['url']
                p = subprocess.Popen(['cvlc','--aout','alsa','-d', url], stdout=subprocess.PIPE)
                out, err = p.communicate()
        
def main():
    """
    Programa principal con bucle infinito
    """
    tree = ET.parse('emisoras.xml')
    root = tree.getroot()
    r = reproductor(1,len(root)) 
    r.play()
    buttons_init()
    lcd_init()
    while True:
        """Este bucle es valido para formato terminal, para el GPIO hay que modificar la lectura"""
        option = {1:r.play,2:r.prev,3:r.next}
        #num=int(raw_input())
        num=buttons.press()
        """inicio de la lectura de GPIO play/rew/foward"""
        if num in option:
            option[num]()

if __name__== '__main__':
    main()
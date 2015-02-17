#Programa de radio streaming para Raspberry con lcd 16x2
import xml.etree.ElementTree as ET
import os
import subprocess, signal
#import lcd
#from lcd.lcd import lcd_init, show


class reproductor:
    id = 1
    def __init__(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setid(self,id):
        self.id=id
    def display(self):
        tree = ET.parse('emisoras.xml')
        root = tree.getroot()
        for child in root:
            if int(child.attrib['id']) == int(self.getid()):
                print child.attrib['id'],"-",child.attrib['freq'],"-",child.attrib['name']
                #show(child.attrib['name'],child.attrib['freq'])
        
    def exit(self):
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if 'vlc' in line:
                pid = int(line.split(None, 1)[0])
                print pid
                os.kill(pid, signal.SIGKILL)
        
    def prev(self):
        if self.getid() == 1:
            self.setid(30)
        else:
            self.setid(self.getid() - 1)
        self.play()
        
    def next(self):
        if self.getid() == 30:
            self.setid(1)
        else:
            self.setid(self.getid() + 1)
        self.play()
        
    def up(self):
        print "up"
        
    def down(self):
        print "down"
        
    def play(self):
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if 'vlc' in line:
                pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)
        self.display()
        tree = ET.parse('emisoras.xml')
        root = tree.getroot()
        for child in root:
            if int(child.attrib['id']) == int(self.getid()):
                url = child.attrib['url']
                p = subprocess.Popen(['cvlc','-d', url], stdout=subprocess.PIPE)
                out, err = p.communicate()
                #subprocess.call(["cvlc", url, "&"])
                #print child.tag, child.attrib['url'],child.attrib['id']
        
def main():
    r = reproductor(1) 
    r.play()
    #lcd_init()
    while True:
        num=int(raw_input())
        option = {0:r.exit,1:r.play,2:r.prev,3:r.next,4:r.up,5:r.down}
        if num in option:
            option[num]()

if __name__== '__main__':
    main()
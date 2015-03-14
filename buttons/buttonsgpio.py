#Fichero de configuracion de los botones del GPIO
#Para cambiar las emisoras
#PLAY = 2 #MOSI
#REW = 3  #MISO
#FOW = 4 #CLK
#ejemplos de GPIO In/out
#http://tipsraspberry.blogspot.com.es/2014/02/gpio-entradas-y-salidas-en-python.html
#boton rew y fow a la vez se para la reproduccion

import time
import RPi.GPIO as GPIO

PLAY = 9
REW = 10
FOW = 11

def buttons_init():
    GPIO.setmode(GPIO.BCM)     # Use BCM GPIO numbers
    GPIO.setup(PLAY, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # play
    GPIO.setup(REW, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # rew
    GPIO.setup(FOW, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # fow
      
def press():
    if GPIO.input(PLAY) == True  & GPIO.input(REW)== False & GPIO.input(FOW)==False:
        time.sleep(3)
        if GPIO.input(PLAY) == True  & GPIO.input(REW)== False & GPIO.input(FOW)==False:
            return 4
        else:
            return 1
    if GPIO.input(PLAY) == False  & GPIO.input(REW)== True & GPIO.input(FOW)==False:
        return 2
    if GPIO.input(PLAY) == False  & GPIO.input(REW)== False & GPIO.input(FOW)==True:
        return 3
    
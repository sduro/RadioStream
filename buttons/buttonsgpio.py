#Fichero de configuracion de los botones del GPIO
#Para cambiar las emisoras

import time
import RPi.GPIO as GPIO

PLAY = 2
REW = 3
FOW = 4

def buttons_init():
    GPIO.setmode(GPIO.BCM)     # Use BCM GPIO numbers
    GPIO.setup(PLAY, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # play
    GPIO.setup(REW, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # rew
    GPIO.setup(FOW, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # fow
      
def press():
    
    if GPIO.input(PLAY):
        return 1
    if GPIO.input(REW):
        return 2
    if GPIO.input(FOW):
        return 3
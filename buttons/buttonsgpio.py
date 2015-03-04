import time
import RPi.GPIO as GPIO

PLAY = 2
REW = 3
FOW = 4

def buttons_init():
    GPIO.setmode(GPIO.BCM)     # Use BCM GPIO numbers
    GPIO.setup(PLAY, GPIO.IN) # E
    GPIO.setup(REW, GPIO.IN)  # RS
    GPIO.setup(FOW, GPIO.IN)  # DB4
   
        
def press():
    if GPIO.input(PLAY):
        return 1
    if GPIO.input(REW):
        return 2
    if GPIO.input(FOW):
        return 3
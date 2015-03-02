import time
import RPi.GPIO as GPIO

PLAY = 2
REW = 3
FOW = 4

def press():
    if GPIO.in(PLAY):
        return 1
    if GPIO.in(REW):
        return 2
    if GPIO.in(FOW):
        return 3
    
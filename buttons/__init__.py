import time
import RPi.GPIO as GPIO

PLAY = 2
REW = 3
FOW = 4

def press():
    if GPIO.input(PLAY):
        return 1
    if GPIO.input(REW):
        return 2
    if GPIO.input(FOW):
        return 3
    
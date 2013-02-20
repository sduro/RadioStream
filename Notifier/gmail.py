#!/usr/bin/env python

import time
#from RPi import GPIO, feedparser

import RPi.GPIO as GPIO, feedparser

USERNAME="sergiduro@gmail.com"
PASSWORD="QDdKRnpU"

#GPIO_PIN=12
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(GPIO_PIN,GPIO.OUT)
 
response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
unread_count = int(response["feed"]["fullcount"])
 
for i in range(0,unread_count):
	print "(" + str((i+1)) + "/" + str(unread_count) + ") " + response['items'][i].title
#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO #gets GPIO pins and call them as GPIO.

GPIO.setmode (GPIO.BCM)
INPUT_PIN = 4 # BCM 23
GPIO.setup (INPUT, GPIO.IN) # set this input pin to be an input.

# create a function to run when the pin is high.
def inputLow (channel) :
	print ('0')

# wait fot the input to go low and run the function when it does.
GPIO.add_event_detect (INPUT_PIN, GPIO.FALLING, callback = inputLow, bouncetime = 200)

# start infinite loop.
while True:
	print ('3,3')
	sleep(1)

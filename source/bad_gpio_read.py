#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
INPUT_PIN_LOW = 4
INPUT_PIN_HIGH = 5
GPIO.setup (INPUT_PIN_LOW, GPIO.IN)
GPIO.setup (INPUT_PIN_HIGH, GPIO.IN)

def get_force():
	if (GPIO.input(INPUT_PIN_HIGH) and GPIO.input(INPUT_PIN_LOW)):
		return 3
	elif (GPIO.input(INPUT_PIN_HIGH) and not GPIO.input(INPUT_PIN_LOW)):
		return 2
	elif (not GPIO.input(INPUT_PIN_HIGH) and GPIO.input(INPUT_PIN_LOW)):
		return 1
	elif (not GPIO.input(INPUT_PIN_HIGH) and not GPIO.input(INPUT_PIN_LOW)):
		return 0
	else:
		return -1




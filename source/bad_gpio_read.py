#!/usr/bin/python

from time import sleep
import serial, threading, time

ser = serial.Serial('/dev/ttyACM1', 9600)
value = 0

def get_force():
	global value
	try:
		state = ser.readline()
		value = int(state)
	except:
		pass
	print value
	return value
		
	


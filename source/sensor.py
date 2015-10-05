#!/usr/bin/python
 
#import smbus
import math
import thread
import time
import smbus

def read_byte(bus, adr):
    return bus.read_byte_data(address, adr)
 
def read_word(bus, adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val
 
def read_word_2c(bus, adr):
    val = read_word(bus, adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

class Sensor():
	bus = smbus.SMBus(1)
	# Power management registers
	power_mgmt_1 = 0x6b
	power_mgmt_2 = 0x6c
	def __init__(self, accelerometer_addr, update_function):
		def update_data (bus, accelerometer_addr, update_function):
			delay = 0.1
			threshold = 0.1 
			
			accel_xout = read_word_2c(bus, 0x3b)
			accel_yout = read_word_2c(bus, 0x3d)
			accel_zout = read_word_2c(bus, 0x3f)
 
			accel_xout_scaled = accel_xout / 16384.0
			accel_yout_scaled = accel_yout / 16384.0
			accel_zout_scaled = accel_zout / 16384.0

			if abs(accel_xout_scaled) > threshold or abs(accel_yout_scaled) > threshold:
				print "Change Data!"
				update_function(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
			time.sleep(delay)

		bus.write_byte_data(accelerometer_addr, power_mgmt_1, 0)
		thread.start_new_thread(update_data, (Sensor.bus, accelerometer_addr, update_function))
		self.accelerometer_addr = accelerometer_addr
		self.update_function = update_function

def f(data):
	print data
s = Sensor(0x68, data)

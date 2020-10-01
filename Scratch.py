#!/usr/bin/env python
import serial
import time

port = '/dev/ttyACM0'

ard = serial.Serial(port, 9600, timeout=5)
time.sleep(2)

i=0

while(i<4):

	setTempCar = 63
	ard.flush()
	setTemp = str(setTempCar)
	print("Python value sent: ")
	print(SetTemp)
	ard.write(str.encode(setTemp))
	time.sleep(1)

	msg = ard.read(ard.inWaiting())
	print("Message from Arduino: ")
	print(msg)
	i = i+1

else:

	print("Exiting")
	exit()


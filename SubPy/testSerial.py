import sys, serial, re, time

port = '/dev/ttyUSB0'
ardPort = '/dev/ttyACM0'
baud = 115200

ard = serial.Serial(ardPort,9600,timeout=5)
time.sleep(2)

ser = serial.Serial(port, baud)
ser.flush()

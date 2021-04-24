import serial, sys, time

ardPort = '/dev/ttyACM0'
ard = serial.Serial(ardPort, 9600,timeout=5)
time.sleep(3)
ard.flush()

print("WARNING: once started the arduino will not stop until code finishes or power is removed")
entry = raw_input("start program? (y/n): ")
if (str(entry.lower()) == "y"):
	print("starting...")
	ard.write("start")
else :
	print("exiting")

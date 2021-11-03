import serial, sys, time

ardPort = '/dev/ttyACM0'
ard = serial.Serial(ardPort, 9600,timeout=5)
time.sleep(3)
ard.flush()

def main():
	print("THIS PROGRAM IS NOT READY TO BE TESTED PLEASE SEE v4")

	print("WARNING: once started the arduino will not stop until code finishes or power is removed")
	entry = raw_input("start program? (y/n): ")
	if (str(entry.lower()) == "y"):
		print("starting...")
	
		print("\n\nCommands:\nStop command: stop\nForward command: fwd\nNeutral command: neut\nDive command: dive\nHover Forward Command: hoverf\nHover Spin command: hovers\n\n")
		ard.write("start")
		entry = "";
		while(str(entry.lower()) != "stop"):
			entry = raw_input("command: ")
			entry = str(entry.lower())
			if(entry == "fwd"):
				ard.write("forward")
			elif (entry == "neut") :
				ard.write("neutral")
			elif (entry == "dive"):
				ard.write("dive")
			elif (entry == "hoverf"):
				ard.write("hoverForward")
			elif (entry == "hovers"):
				ard.write("hoverSpin")
			elif (entry == "stop"):
				ard.write("kill")
			else :
				print("command not recognized... crashing")
				break	
			getSerialDone()

		ard.write("kill")
	
	else :
		print("exiting")


def getSerialDone():
	s = None
	while(s == "done"):
		s = ard.read(100)
		s = str(s).lower()
	return s

main()

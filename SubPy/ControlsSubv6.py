import serial, sys, time


def getSerialDone():
    s = None
    while (s != "status: done"):
        s = ard.readline().decode('utf-8').rstrip()
        if (s != ""):
            print(s)
        if (s == "status: killed"):
            return
        time.sleep(1)
    return


def printSerial():
    line = ard.readline().decode('utf-8').rstrip()
    if (line != ""):
        print(line)
    time.sleep(1)
    return


def waitForSerial(reciept):
    s = None
    while (s != reciept):
        s = ard.readline().decode('utf-8').rstrip()
        if (s != ""):
            print(s)
        if (s == "status: killed"):
            return
        time.sleep(1)
    return


ardPort = '/dev/ttyACM0'
baud = 115200
time_out = 1
ard = serial.Serial(ardPort, baud, timeout=time_out)
time.sleep(1)
ard.flush()

if __name__ == '__main__':
    print("WARNING: once started the arduino will not stop until code finishes or power is removed")
    print("WARNING: use keyboard interrupt to stop as fast as possible: ctrl+c")
    entry = input("start program? (y/n): ")
    if (str(entry.lower()) == "y"):
        print()
        print("starting...")
        ard.write(b"start\n")
        waitForSerial("arduino ready")
        ard.flush()
        print(
            "\n\nCommands:\nStop command: stop\nKill command: kill\nForward command: fwd\nReverse command: rvs\nNeutral command: neut\nDive command: dive\nHover Forward Command: hover_f\nHover Spin command: hover_s\nTest all motors command: test_all\nTest all motors sequentially command: seq_test\n\n")
        kill_flag = 0
        entry = ""
        try:
            while (kill_flag == 0):
                entry = input("\ncommand: ")
                entry = str(entry.lower())
                if (entry == "fwd"):
                    ard.write(b"forward\n")
                elif (entry == "rvs"):
                    ard.write(b"reverse\n")
                elif (entry == "neut"):
                    ard.write(b"neutral\n")
                elif (entry == "dive"):
                    ard.write(b"dive\n")
                elif (entry == "hover_f"):
                    ard.write(b"hoverForward\n")
                elif (entry == "hover_s"):
                    ard.write(b"hoverSpin\n")
                elif (entry == "test_all"):
                    ard.write(b"all\n")
                elif (entry == "seq_test"):
                    ard.write(b"seqTest\n")
                elif (entry == "stop"):
                    ard.write(b"kill\n")
                    kill_flag = 1
                elif (entry == "kill"):
                    ard.write(b"kill\n")
                    kill_flag = 1
                else:
                    print("command not recognized")
                    continue
                getSerialDone()
        except KeyboardInterrupt:
            ard.write(b"kill\n")
            print("\n\narduino kill command sent\n")
            waitForSerial("recived: kill")
        ard.write(b"kill\n")
        print("\nexiting script...\n\n")
    else:
        print("exiting")

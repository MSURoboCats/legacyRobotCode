# Capstone team RAVN: 2020 - 2021
# Members: Scott Smith, Kyle Rust, Tristan Stevens

import math
import numpy as np
import re
import serial
import sys
import time

import central_nervous_system as cns
import sensory_system as ss

# Initialize constants ---------------------------------------------
ARDUINO_BAUD = 9600
ARDUINO_PORT = '/dev/ttyACM1'
ARDUINO = serial.Serial(ARDUINO_PORT, ARDUINO_BAUD, timeout=5)
DELTA = 1
DEPTH_KD = .25286
DEPTH_KP = 1.178
MAX_THROTTLE_OUT = 1900
MID_THROTTLE_OUT = 1500
MIN_THROTTLE_OUT = 1100
NUC_BAUD = 115200
NUC_PORT = '/dev/ttyUSB0'
NUC = serial.Serial(NUC_PORT, NUC_BAUD)
PITCH_KD = .15406
PITCH_KP = .3309
ROLL_KD = .15406
ROLL_KP = .3309
YAW_KD = .25684
YAW_KP = .58395

# Initialize variables ---------------------------------------------
depth_error_n = 0
depth_error_n_minus_1 = 0
depth_n_minus_1 = 0
depth_n = 0

pitch_error_n = 0
pitch_error_n_minus_1 = 0
pitch_n = 0
pitch_n_minus_1 = 0

roll_error_n = 0
roll_error_n_minus_1 = 0
roll_n = 0
roll_n_minus_1 = 0

yaw_error_n = 0
yaw_error_n_minus_1 = 0
yaw_n = 0
yaw_n_minus_1 = 0

# Define functions -------------------------------------------------
def bound_throttle_out(desired_throttle):
    return max(min(MAX_THROTTLE_OUT, desired_throttle), MIN_THROTTLE_OUT)


def normalize(desired_result):
    return max(min(1, desired_result), -1)


def quaternion_to_euler(data):
    yz2 = 1 - (2 * (data[1]**2 + data[2]**2))
    pitch_p = 2 * (data[0] * data[2] - data[3] * data[1])
    roll_p = (2 * (data[0] * data[1] + data[2] * data[3])) / yz2
    yaw_p = (2 * (data[0] * data[3] + data[1] * data[2]))
    
    pitch_p = 1 if pitch_p > 1 else pitch_p
    pitch_p = -1 if pitch_p < -1 else pitch_p

    roll = math.atan(roll_p)
    pitch = math.asin(pitch_p)  
    yaw = math.atan2(yaw_p,yz2) + math.pi 

    #print("Roll: %s" % roll)
    #print("Pitch: %s" % pitch)
    #print("Yaw: %s" % yaw)

    return [roll, pitch, yaw]


def update_imu_data():
    mag = []    # w, x, y, z
    NUC.write("$PSPA,QUAT\r\n")
    data = NUC.readline()
    values = np.array(re.findall('([-\d.]+)', data)).astype(np.float)
    magnetometer = values
    mag = [magnetometer[i] for i in range(4)]
    roll_n, pitch_n, yaw_n = quaternion_to_euler(mag)
    if(yaw_n > math.pi):
        yaw_n = yaw_n - 2*math.pi


#Looks to be a test to see what depth the sub is at -ZW
def depth_func(desired_depth):
    update_imu_data()
    depth_error_n_minus_1 = depth_error_n
    depth_error_n = desired_depth - depth_n
    result = DEPTH_KP*depth_error_n + DEPTH_KD*((depth_error_n - depth_error_n_minus_1)/DELTA)
    return normalize(result)


# Currently, pitch function should always act to maintain neutral pitch
def pitch_func():
    update_imu_data()
    pitch_error_n_minus_1 = pitch_error_n
    pitch_error_n = 0 - pitch_n
    result = PITCH_KP*pitch_error_n + PITCH_KD*((pitch_error_n - pitch_error_n_minus_1)/DELTA)
    return normalize(result)


# Currently, roll function should always act to maintain neutral roll
def roll_func():
    update_imu_data()
    roll_error_n_minus_1 = roll_error_n
    roll_error_n = 0 - roll_n
    result = ROLL_KP*roll_error_n + ROLL_KD*((roll_error_n - roll_error_n_minus_1)/DELTA)
    return normalize(result)


def yaw_func(desired_yaw):
    update_imu_data()
    yaw_error_n_minus_1 = yaw_error_n
    yaw_error_n = desired_yaw - yaw_n
    result = YAW_KP*yaw_error_n + YAW_KD*((yaw_error_n - yaw_error_n_minus_1)/DELTA)
    return normalize(result)


#Here's the throttle control that uses what looks like 7 or 8 different speed settings, this might be useful to take a look at -ZW
#Rudimentary Throttle Control
def ThrottleOut():
    T6 = depth_func() + roll_func() + pitch_func()
    T5 = -(depth_func() + roll_func() - pitch_func())
    T8 = -(depth_func() - roll_func() + pitch_func())
    T7 = depth_func() - roll_func() - pitch_func()
    T4 = 1500 #-1*yaw_func()
    T3 = 1500 #yaw_func()
    T1 = 1500
    T2 = 1500
    if (T7 > 1):
        T7 = 1900
    elif(T7 < -1):
        T7 = 1100
    else:
        T7 = int(400*T7 + 1500)

    if (T8 > 1):
        T8 = 1900
    elif(T8 < -1):
        T8 = 1100
    else:
        T8 = int(400*T8 + 1500)

    if (T3 > 1):
        T3 = 1900
    elif(T3 < -1):
        T3 = 1100
    else:
        T3 = int(400*T3 + 1500)        

    if (T4 > 1):
        T4 = 1900
    elif(T4 < -1):
        T4 = 1100
    else:
        T4 = int(400*T4 + 1500)

    if (T5 > 1):
        T5 = 1900
    elif(T5 < -1):
        T5 = 1100
    else:
        T5 = int(400*T5 + 1500)
    
    if (T6 > 1):
        T6 = 1900
    elif(T6 < -1):
        T6 = 1100
    else:
        T6 = int(400*T6 + 1500)

    #print ("Values sent: ")
    #print(T1,T2,T3,T4,T5,T6,T7,T8)
    ARDUINO.write(str.encode(str(T1))+" "+str.encode(str(T2))+" "+str.encode(str(T3))+" "+str.encode(str(T4))+" "+str.encode(str(T5))+" "+str.encode(str(T6))+" "+str.encode(str(T7))+" "+str.encode(str(T8))+" ")
    time.sleep(.1)

    return T1, T2, T3, T4, T5, T6, T7, T8

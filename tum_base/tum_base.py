##base.py is for communicating with the arduino that controlls the robot base

import time
import serial
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
while True:
    commandString = input("Command: ")
    comByte = bytes(commandString, 'utf-8')
    ser.write(comByte)

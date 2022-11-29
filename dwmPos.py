#Python wrapper for reading the position data from DWM1001 tag
#The tag is programmed with firmware from the tutorial, input of "apg" yields position data
#The goal of this script is to read the serial port and pass it to wherever I need it to go

import time
import serial
ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
while True:
    time.sleep(1)
    ser.write(b"apg\n")
    #the output format is in x: y: z: qf: , we can use that to parse
    raw_dwm_out = ser.read(50)
    
    x_value =  raw_dwm_out.partition(b"x:")[2].partition(b" y:")[0]     #Isolates the value of x: 
    y_value = raw_dwm_out.partition(b"y:")[2].partition(b" z:")[0]   #trying to combine them
    z_value = raw_dwm_out.partition(b"z:")[2].partition(b" qf:")[0] 

    print("x:",x_value," y:",y_value," z:", z_value)

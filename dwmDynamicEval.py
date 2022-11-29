#Python wrapper for reading the position data from DWM1001 tag
#The tag is programmed with firmware from the tutorial, input of "apg" yields position dat
#This script is for collecting data to evaluate accuracy with dynamic positioning

import time
import csv
import serial
import math 

SIZEOFSERIES = 60
trial_name = input("Trial Name:")
ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
file = open(trial_name + ".csv",'w')
csvWriter = csv.writer(file)
dataHeaders = ['x','y','z']
csvWriter.writerow(dataHeaders)

data = []
for i in range(SIZEOFSERIES):
    time.sleep(.1)
    ser.write(b"apg\n")
    #the output format is in x: y: z: qf: , we can use that to parse
    raw_dwm_out = ser.read(50)
    x_value = int(raw_dwm_out.partition(b"x:")[2].partition(b" y:")[0].decode())     #Isolates the value of x: 
    y_value = int(raw_dwm_out.partition(b"y:")[2].partition(b" z:")[0].decode())   
    z_value = int(raw_dwm_out.partition(b"z:")[2].partition(b" qf:")[0].decode())  
    
    data.append([x_value,y_value,z_value])
    print([x_value,y_value,z_value])

csvWriter.writerows(data)
file.close()



##Functionally, the only thing this code does is  collect the position data for a minute
#We will have to have a prediscribed path for the tag to follow
# we can create a triangle and move to those positions.

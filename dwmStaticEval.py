#Python wrapper for reading the position data from DWM1001 tag
#The tag is programmed with firmware from the tutorial, input of "apg" yields position data
#The goal of this script is to read the serial port and pass it to wherever I need it to go

import time
import csv
import serial
import math 

SIZEOFSERIES = 100
#prompt user for test info
trial_name = input("Trial Name:\n")
true_x_value = input("True X value:\n")
true_y_value = input("True Y value:\n")
true_z_value = input("True Z value:\n")
true_coordinates = [int(true_x_value), int(true_y_value), int(true_z_value)]

ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
file = open(trial_name + ".csv",'w')
csvWriter = csv.writer(file)
dataHeaders = ['x','y','z','error','reference',true_coordinates]
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
    
    error = math.dist([x_value,y_value,z_value], true_coordinates) #pythagorean distance formula
    data.append([x_value,y_value,z_value,error])
    print([x_value,y_value,z_value,error])

csvWriter.writerows(data)
file.close()



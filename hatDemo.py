from sense_hat import SenseHat
import time
import serial
ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
hat = SenseHat()
hat.set_rotation(180)
hat.clear()
#get the demensions of the grid 
grid_bounds = (1727,1727)
#write a function to size out the grid to the demensions of the sense hat
    #if the x or y coordinate is out of bound then the board should light up red 
    #the color should go from green to blue based on if z is positive or negative
def hat_position(x,y,z,bound_x,bound_y):
    if z > 0:
        dot_color = (0,200,0)
    else:
        dot_color = (0,0,200)
    if x > bound_x or y > bound_y or x < 0 or y < 0:
        print("out of bounds: ",x,y,z,bound_x,bound_y)
        hat.clear(200,0,0);
    else:
       #grid for the sense hat is 8x8 numbered 0-7
       dot_x = int(x / (bound_x/8))
       dot_y = int(y / (bound_y/8))
       print("Displaying Coordinate:",dot_x,dot_y)
       hat.clear()
       hat.set_pixel(dot_x,dot_y,dot_color)
sample_count = 0
coordinate_avg = [0,0,0]
sample_limit = 5
while(True):
     ser.write(b"apg\n")
     #the output format is in x: y: z: qf: , we can use that to parse
     raw_dwm_out = ser.read(50)
     x_value = int(raw_dwm_out.partition(b"x:")[2].partition(b" y:")[0].decode()) 
     y_value = int(raw_dwm_out.partition(b"y:")[2].partition(b" z:")[0].decode())   
     z_value = int(raw_dwm_out.partition(b"z:")[2].partition(b" qf:")[0].decode())
     sample_count += 1
        
     if sample_count < sample_limit:
         coordinate_avg[0] += x_value
         coordinate_avg[1] += y_value
         coordinate_avg[2] += z_value
     else:
        coordinate_avg[0] /= sample_limit
        coordinate_avg[1] /= sample_limit
        coordinate_avg[2] /= sample_limit
        hat_position(*coordinate_avg,*grid_bounds)
        coordinate_avg = [0,0,0]
        sample_count = 0


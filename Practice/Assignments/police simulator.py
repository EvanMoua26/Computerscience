from adafruit_circuitplayground import cp

import time
#when the program finishes hte board enters a waiting state
#-> flashes all green then off
# We do not want the program to ever end
#thats why we put our program in a will true
#-> runs forever
while True:
    cp.pixels[0] = (0,1,0)
    cp.pixels[1] =(0,1,0)
    cp.pixels[2] =(0,1,0)
    cp.pixels[3] = (0,1,0)
    cp.pixels[4] = (0,1,0)
    cp.pixels[5] = (0,1,0)  
    cp.pixels[6] = (0,1,0)
    cp.pixels[7] = (0,1,0)
    cp.pixels[8] = (0,1,0)
    cp.pixels[9] = (0,1,0)
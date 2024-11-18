from adafruit_circuitplayground import cp
import time
#cp.pixels.brightness = .01

while True:      #everything goes in here
    #how to interact with pixel
    #0-255
    if cp.switch:
        cp.pixels[0] = (0,1,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
        cp.pixels[1] = (0,1,0)
        cp.pixels[2] = (0,1,0)
        cp.pixels[3] = (0,1,0)
        cp.pixels[4] = (0,1,0)
        cp.pixels[5] = (0,0,0)
        cp.pixels[6] = (0,0,0)
        cp.pixels[7] = (0,0,0)
        cp.pixels[8] = (0,0,0)
        cp.pixels[9] = (0,0,0)
    else:
        cp.pixels[0] = (0,0,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
        cp.pixels[1] = (0,0,0)
        cp.pixels[2] = (0,0,0)
        cp.pixels[3] = (0,0,0)
        cp.pixels[4] = (0,0,0)
        cp.pixels[5] = (0,1,0)
        cp.pixels[6] = (0,1,0)
        cp.pixels[7] = (0,1,0)
        cp.pixels[8] = (0,1,0)
        cp.pixels[9] = (0,1,0)
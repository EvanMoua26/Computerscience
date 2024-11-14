from adafruit_circuitplayground import cp
import time
#cp.pixels.brightness = .01

while True:      #everything goes in here
    if cp.button_a:
        time.sleep(0.1)
        cp.pixels[0] = (0,0,1) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
        time.sleep(0.1)
        cp.pixels[0] = (0,0,0)
        cp.pixels[1] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[1] = (0,0,0)
        cp.pixels[2] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[2] = (0,0,0)
        cp.pixels[3] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[3] = (0,0,0)
        cp.pixels[4] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[4] = (0,0,0)
        cp.pixels[5] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[5] = (0,0,0)
        cp.pixels[6] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[6] = (0,0,0)
        cp.pixels[7] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[7] = (0,0,0)
        cp.pixels[8] = (0,0,1)
        time.sleep(0.1)
        cp.pixels[8] = (0,0,0)
        cp.pixels[9] = (0,0,1)
        time.sleep(.1) # Blue

        while cp.button_a:  # Wait until button is released
            pass
    else:
             cp.pixels.fill((0,0,0)) # Off
from adafruit_circuitplayground import cp
import time
import random
while True: # Threshold to detect significant motion
    x, y, z = cp.acceleration  # Get acceleration along X, Y, Z axes
    shake_threshold = 15.0  # Example threshold value
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        range = random.randint(1,256)
        rang = random.randint(1,256)
        ran = random.randint(1,256)
        cp.pixels[0] = (ran,ran,ran)
        cp.pixels[1] = (range,rang,ran)
        cp.pixels[2] = (range,range,rang)
        cp.pixels[3] = (ran,rang,ran)
        cp.pixels[4] = (range,rang,ran)
        cp.pixels[5] = (rang,range,rang)
        cp.pixels[6] = (ran,rang,ran)
        cp.pixels[7] = (range,range,ran)
        cp.pixels[8] = (range,rang,range)
        cp.pixels[9] = (range,ran,range)
        cp.pixels.brightness = .01
        
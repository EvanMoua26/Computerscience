from adafruit_circuitplayground import cp
import time

lit_pixels = 0

while True:
    if cp.button_a:
     
        if lit_pixels < len(cp.pixels):
            cp.pixels[lit_pixels] = (0, 0, 225) 
            lit_pixels += 1
            time.sleep(0.2)  

    if cp.button_b:
     
        if lit_pixels > 0:
            lit_pixels -= 1
            cp.pixels[lit_pixels] = (0, 0, 0) 
            time.sleep(0.2) 
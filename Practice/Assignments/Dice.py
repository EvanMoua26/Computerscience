import time
import random
from adafruit_circuitplayground import cp


# Function to turn off all pixels
def turn_off_pixels():
    cp.pixels.fill((0, 0, 0))  # Set all pixels to black (off)

# Function to light up a certain number of pixels
def light_up_pixels(num_pixels):
    # Ensure we don't try to light up more than the available pixels
    num_pixels = min(num_pixels, len(cp.pixels))
    for i in range(num_pixels):
        cp.pixels[i] = (0, 255, 0)

while True:
   
    if cp.button_a:
     
        num = random.randint(1, 10)
        light_up_pixels(num)
        time.sleep(0.5)  
    if cp.button_b:
        turn_off_pixels() 
        time.sleep(0.5)
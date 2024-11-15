# first need to import board specific tools
#every project for this board will need this statment
import board
import digitalio
import neopixel
import time

# Setup the switch pin (assuming the switch is connected to pin D5)
switch_pin = digitalio.DigitalInOut(board.D7)
switch_pin.switch_to_input(pull=digitalio.Pull.UP)

# Setup the NeoPixels (Circuit Playground has 10 NeoPixels)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=True)

# Function to turn on/off pixels based on the switch position
def update_pixels():
    if switch_pin.value:  # Switch is in the left position (HIGH)
        # Turn pixels 0-4 off, pixels 5-9 green on 
        for i in range(5):
            pixels[i] = (0, 0, 0)  # Off
        for i in range(5, 10):
            pixels[i] = (0, 255, 0)  # Green
    else:  # Switch is in the right position (LOW)
        # Turn pixels 0-4 green off , pixels 5-9 off
        for i in range(5):
            pixels[i] = (0, 255, 0)  # Green
        for i in range(5, 9):
            pixels[i] = (0, 0, 0)  # Off

# Main loop
while True:
    update_pixels()
    time.sleep(0.1)  # Update every 100ms to reduce flicker and CPU load


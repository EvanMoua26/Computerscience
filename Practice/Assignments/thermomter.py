
from adafruit_circuitplayground import cp
import time

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

while True:
    # Get the current temperature in Celsius and convert to Fahrenheit
    temperature_f = celsius_to_fahrenheit(cp.temperature)

    # Display the temperature for debugging (optional)
    print("Temperature (F):", temperature_f)

    # Turn on/off pixels based on the temperature ranges
    if temperature_f < 78:
        cp.pixels[0] = (0, 0, 1)  # Blue for Pixel 0
    else:
        cp.pixels[0] = (0, 0, 0)  # Off for Pixel 0

    if temperature_f > 78:
        cp.pixels[1] = (0, 0, 1)  # Blue for Pixel 1
    else:
        cp.pixels[1] = (0, 0, 0)  # Off for Pixel 1

    if temperature_f > 79:
        cp.pixels[2] = (0, 0, 1)  # Blue for Pixel 2
    else:
        cp.pixels[2] = (0, 0, 0)  # Off for Pixel 2

    if temperature_f > 80:
        cp.pixels[3] = (1, 1, 0)  # Yellow for Pixel 3
    else:
        cp.pixels[3] = (0, 0, 0)  # Off for Pixel 3

    if temperature_f > 81:
        cp.pixels[4] = (1, 1, 0)  # Yellow for Pixel 4
    else:
        cp.pixels[4] = (0, 0, 0)  # Off for Pixel 4

    if temperature_f > 82:
        cp.pixels[5] = (1, 1, 0)  # Yellow for Pixel 5
    else:
        cp.pixels[5] = (0, 0, 0)  # Off for Pixel 5

    if temperature_f > 83:
        cp.pixels[6] = (1, 1, 0)  # Yellow for Pixel 6
    else:
        cp.pixels[6] = (0, 0, 0)  # Off for Pixel 6

    if temperature_f > 84:
        cp.pixels[7] = (1, 0, 0)  # Red for Pixel 7
    else:
        cp.pixels[7] = (0, 0, 0)  # Off for Pixel 7

    if temperature_f > 85:
        cp.pixels[8] = (1, 0, 0)  # Red for Pixel 8
    else:
        cp.pixels[8] = (0, 0, 0)  # Off for Pixel 8

   

    # Wait a short time before checking the temperature again
    time.sleep(1)


from adafruit_circuitplayground import cp
import time

# Define the frequencies for the siren tones
tone_1 = 500  # 500 Hz
tone_2 = 900  # 900 Hz

while True:
    # Flash all pixels red
    cp.pixels.fill((255, 0, 0))  # Red color
    cp.play_tone(tone_1, 0.5)  # Play 500 Hz tone for 0.5 seconds
    time.sleep(0.5)  # Wait for 500ms

    # Flash all pixels blue
    cp.pixels.fill((0, 0, 255))  # Blue color
    cp.play_tone(tone_2, 0.5)  # Play 900 Hz tone for 0.5 seconds
    time.sleep(0.5)  # Wait for 500ms

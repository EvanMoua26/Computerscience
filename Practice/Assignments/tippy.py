from adafruit_circuitplayground import cp
import time

# Set the tilt threshold for detecting left and right tilt
tilt_threshold = 5.0  # Adjust the sensitivity if needed

while True:
    x, y, z = cp.acceleration  # Get acceleration values along X, Y, Z axes

    # Check for tilt to the left (negative X) or to the right (positive X)
    if x < -tilt_threshold:  # Tilted to the left
     
        cp.pixels[6] = (0, 255, 0)  # Green
        cp.pixels[7] = (0, 255, 0)  # Green
        cp.pixels[8] = (0, 255, 0)  # Green

        # 
        cp.pixels[1] = (0, 0, 0)    # Off
        cp.pixels[2] = (0, 0, 0)    # Off
        cp.pixels[3] = (0, 0, 0)    # Off

    elif x > tilt_threshold:  # Tilted to the right
       
        cp.pixels[1] = (0, 225, 0)  # green
        cp.pixels[2] = (0, 225, 0)  # green
        cp.pixels[3] = (0, 225, 0)  # green

       
        cp.pixels[6] = (0, 0, 0)    # Off
        cp.pixels[7] = (0, 0, 0)    # Off
        cp.pixels[8] = (0, 0, 0)    # Off

    else:
       
        cp.pixels[1] = (0, 0, 0)  # Off
        cp.pixels[2] = (0, 0, 0)  # Off
        cp.pixels[3] = (0, 0, 0)  # Off
        cp.pixels[6] = (0, 0, 0)  # Off
        cp.pixels[7] = (0, 0, 0)  # Off
        cp.pixels[8] = (0, 0, 0)  # Off

    time.sleep(0.1)  # Small delay to prevent rapid changes

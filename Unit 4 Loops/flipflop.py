# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp
import time
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever



while True:
    if cp.switch:
        cp.pixels[0] = (255,0,0)
        cp.pixels[1] = (255,0,0)
        cp.pixels[2] = (255,0,0)
        cp.pixels[3] = (255,0,0)
        cp.pixels[4] = (255,0,0)
        cp.pixels[5] = (0,0,0)
        cp.pixels[6] = (0,0,0)
        cp.pixels[7] = (0,0,0)
        cp.pixels[8] = (0,0,0)
        cp.pixels[9] = (0,0,0)
    
    else:
         cp.pixels[0] = (0,0,0)
         cp.pixels[1] = (0,0,0)
         cp.pixels[2] = (0,0,0)
         cp.pixels[3] = (0,0,0)
         cp.pixels[4] = (0,0,0)
         cp.pixels[5] = (255,0,0)
         cp.pixels[6] = (255,0,0)
         cp.pixels[7] = (255,0,0)
         cp.pixels[8] = (255,0,0)
         cp.pixels[9] = (255,0,0)

    time.sleep(0.1)


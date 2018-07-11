# Basic example of using the Bi-color 24 segment bargraph display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Carter Nelson
# License: Public Domain

import time

# Import board related modules
import board
import busio

# Import the Bicolor24 driver from the HT16K33 module
from adafruit_ht16k33.bargraph import Bicolor24

# Create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED bargraph class.
bar = Bicolor24(i2c)

# Set individual segments of bargraph
bar[0] = bar.LED_RED
bar[1] = bar.LED_GREEN
bar[2] = bar.LED_YELLOW

time.sleep(2)

# Turn them all off
bar.fill(bar.LED_OFF)

# Turn them on in a loop
for i in range(24):
    bar[i] = bar.LED_RED
    time.sleep(0.1)
    bar[i] = bar.LED_OFF

time.sleep(1)

# Fill the entrire bargraph
bar.fill(bar.LED_GREEN)

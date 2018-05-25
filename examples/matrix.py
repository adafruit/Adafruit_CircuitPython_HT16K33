# Basic example of clearing and drawing a pixel on a LED matrix display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
from board import *
import busio

# Import the HT16K33 LED matrix module.
from adafruit_ht16k33 import matrix


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the matrix class.
# This creates a 16x8 matrix:
matrix = matrix.Matrix16x8(i2c)
# Or this creates a 8x8 matrix:
#matrix = matrix.Matrix8x8(i2c)
# Or this creates a 8x8 bicolor matrix:
#matrix = matrix.Matrix8x8x2(i2c)
# Finally you can optionally specify a custom I2C address of the HT16k33 like:
#matrix = matrix.Matrix16x8(i2c, address=0x70)

# Clear the matrix.  Always call show after changing pixels to make the display
# update visible!
matrix.fill(0)
matrix.show()

# Set a pixel in the origin 0,0 position.
matrix.pixel(0, 0, 1)
# Set a pixel in the middle 8, 4 position.
matrix.pixel(8, 4, 1)
# Set a pixel in the opposite 15, 7 position.
matrix.pixel(15, 7, 1)
matrix.show()

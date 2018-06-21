# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
from board import *
import busio

# Import the HT16K33 LED segment module.
from adafruit_ht16k33 import segments


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
# Or this creates a 14 segment alphanumeric 4 character display:
#display = segments.Seg14x4(i2c)
# Finally you can optionally specify a custom I2C address of the HT16k33 like:
#display = segments.Seg7x4(i2c, address=0x70)

# Clear the display.  Always call show after changing the display to make the
# update visible!
display.fill(0)
display.show()

# Set the first character to '1':
display[0] = '1'
# Set the second character to '2':
display[1] = '2'
# Set the third character to 'A':
display[2] = 'A'
# Set the forth character to 'B':
display[3] = 'B'
# Make sure to call show to see the changes above on the display!
display.show()

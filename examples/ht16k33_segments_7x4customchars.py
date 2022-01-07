# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Basic example of setting digits on a LED segment display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Alec Delaney
# License: Public Domain

# Import all board pins.
import board
import busio
from adafruit_ht16k33 import segments

# Create the character dictionary
# You can use the list normally referenced as a starting point
custom_chars = {}
typical_list_values = segments.NUMBERS
typical_list_chars = list("0123456789abcdef")
for char, value in zip(typical_list_chars, typical_list_values):
    custom_chars[char] = value

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
display = segments.Seg7x4(i2c, char_dict=)

# Clear the display.
display.fill(0)

# Can just print a number
display.print("42")

# Show a looping marquee
display.marquee("Deadbeef 192.168.100.102... ", 0.2)
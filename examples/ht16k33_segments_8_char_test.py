#  Test program for 8 character 14 segment alphanumeric LED displays
#  This example and library is meant to work with Adafruit CircuitPython API.
#  Author: Paul Bricmont
#  License: Public Domain

import time

#  Import all board pins.
import board
import busio

#  Import the HT16K33 LED 8 character segment module.
from adafruit_ht16k33 import segments_8_char


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

#  Create the LED segment class.
#  Create a 14 segment alphanumeric 8 character display:
display = segments_8_char.Seg14x8(i2c)
#  Optionally, specify a custom I2C address for the HT16k33 chip:
#display = segments_8_char.Seg14x8(i2c, address=0x70)

#  Clear the display.
display.fill(0)

#  Segment Test
#  Light-up all the segments of each character, one character at a time
i = 0

for i in range(8):
    display[i] = chr(127)
    time.sleep(1)
    display.fill(0)
    i += 1

time.sleep(1)

#  print an integer
display.print(123456)
time.sleep(3)
display.fill(0)
#  print a floating point number
display.print(3.14159)
time.sleep(3)
display.fill(0)

time.sleep(1)

#  Print all supported alphanumeric characters 8 at a time
i = 33

for i in range(33, 127, 8):
    string = chr(i) + chr(i + 1) + chr(i + 2) + chr(i + 3) + chr(i + 4) + chr(i + 5) + chr(i + 6) + chr(i + 7)
    display.print(string)
    time.sleep(3)
    i += 1

time.sleep(1)

#  print a string
display.print('ADAFRUIT')
time.sleep(3)
display.fill(0)

#  Set individual characters
#  Set the first character to 'A':
display[0] = 'A'
#  Set the second character to 'B':
display[1] = 'B'
#  Set the third character to 'C':
display[2] = 'C'
#  Set the forth character to 'D':
display[3] = 'D'
#  Set the fifth character to '1':
display[4] = '1'
#  Set the sixth character to '2':
display[5] = '2'
#  Set the seventh character to '3':
display[6] = '3'
#  Set the eighth character to '4':
display[7] = '4'

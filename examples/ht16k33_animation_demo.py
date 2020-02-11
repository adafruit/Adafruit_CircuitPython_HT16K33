""" Test script for display animations on an HT16K33 with alphanumeric display """

import board
import busio
from time import sleep
from adafruit_ht16k33 import segments

#	The number of seconds to delay between writing segments
DEFAULT_CHAR_DELAY_SEC = 0.2

#	The number of cycles to go for each animation
DEFAULT_CYCLES = 1

#
#	Segment bits on the HT16K33 with alphanumeric display
#

N = 16384
M =  8192
L =  4096
K =  2048
J =  1024
I =   512
H =   256
G2=   128
G1=    64
F =    32
E =    16
D =     8
C =     4
B =     2
A =     1

def animate(digits, bitmasks, delay=DEFAULT_CHAR_DELAY_SEC, cycles=DEFAULT_CYCLES):
	'''
	Main driver for alphanumeric display animations (WIP!!!)
		Param: digits - a list of the digits to write to, like [0, 1, 3]. The digits are 
			0 to 3 starting at the left most digit. Digits will be written to in sequence.
		Param: bitmasks - a list of the bitmasks to write, in sequence, to the specified digits.
		Param: delay - The delay, in seconds (or fractions of), between writing bitmasks to a digit.
		Param: cycles - The number of cycles (loops) to write an animation.

        Returns: No result
	'''
	for cy in range(cycles):
		for dig in digits:
			for bits in bitmasks:
				display.set_digit_raw(dig, bits)
				sleep(delay)

def chase_animation(delay=DEFAULT_CHAR_DELAY_SEC, cycles=DEFAULT_CYCLES):
	for cy in range(cycles):
		animate([0, 1, 2, 3], [A, 0], delay)
		animate([3], [B, C, D, 0], delay)
		animate([2, 1, 0], [D, 0], delay)
		animate([0], [E, F, H, G2, 0], delay)
		animate([1, 2], [G1, G2, 0], delay)
		animate([3], [G1, J, A, 0], delay)
		animate([2, 1], [A, 0], delay)
		animate([0], [A, F, E, D, 0], delay)
		animate([1, 2], [D, 0], delay)
		animate([3], [D, C, B, J, G1, 0], delay)
		animate([2, 1], [G2, G1, 0], delay)
		animate([0], [H, 0], delay)
		#animate([0], [M, H, 0x0], delay)

#	Initialize the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

#	Initialize the HT16K33 with alphanumeric display featherwing
display = segments.Seg14x4(i2c)

text = "Init"

display.fill(1)
sleep(1)
display.fill(0)

display.print(text)
sleep(1)
display.fill(0)
print()

while True:
	#	Arrow
	animate([0, 1, 2], [G1+G2])
	animate([3], [G1+H+K])
	sleep(1.5)
	display.fill(0)
	sleep(1.5)

	#	Flying
	animate([0], [H+J, G1+G2, K+M, G1+G2], 0.2, 5)
	animate([0], [0])
	sleep(1.5)
	display.fill(0)
	sleep(1.5)
	
	#	Chase and reverse.
	chase_animation(0.1, 5)
	sleep(1.5)
	display.fill(0)
	sleep(1.5)

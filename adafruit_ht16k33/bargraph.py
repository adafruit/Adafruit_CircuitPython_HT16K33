# The MIT License (MIT)
#
# Copyright (c) 2018 Carter Nelson for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
`adafruit_ht16k33.bargraph`
===========================

* Authors: Carter Nelson for Adafruit Industries

"""

from adafruit_ht16k33.ht16k33 import HT16K33

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_HT16K33.git"


class Bicolor24(HT16K33):
    """Bi-color 24-bar bargraph display."""

    LED_OFF = 0
    LED_RED = 1
    LED_GREEN = 2
    LED_YELLOW = 3

    def __getitem__(self, key):
        # map to HT16K33 row (x) and column (y), see schematic
        x = key % 4 + 4 * (key // 12)
        y = key // 4 - 3 * (key // 12)
        # construct the color value and return it
        return self._pixel(x, y) | self._pixel(x + 8, y) << 1

    def __setitem__(self, key, value):
        # map to HT16K33 row (x) and column (y), see schematic
        x = key % 4 + 4 * (key // 12)
        y = key // 4 - 3 * (key // 12)
        # conditionally turn on red LED
        self._pixel(x, y, value & 0x01)
        # conditionally turn on green LED
        self._pixel(x + 8, y, value >> 1)

    def fill(self, color):
        """Fill the whole display with the given color."""
        what_it_was = self.auto_write
        self.auto_write = False
        for i in range(24):
            self[i] = color
        self.show()
        self.auto_write = what_it_was

# The MIT License (MIT)
#
# Copyright (c) 2016 Radomir Dopieralski & Tony DiCola for Adafruit Industries
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
Segment Displays
=================
"""

from adafruit_ht16k33.ht16k33 import HT16K33

CHARS = (
    0b00000000, 0b00000000, #
    0b01000000, 0b00000110, # !
    0b00000010, 0b00100000, # "
    0b00010010, 0b11001110, # #
    0b00010010, 0b11101101, # $
    0b00001100, 0b00100100, # %
    0b00100011, 0b01011101, # &
    0b00000100, 0b00000000, # '
    0b00100100, 0b00000000, # (
    0b00001001, 0b00000000, # )
    0b00111111, 0b11000000, # *
    0b00010010, 0b11000000, # +
    0b00001000, 0b00000000, # ,
    0b00000000, 0b11000000, # -
    0b00000000, 0b00000000, # .
    0b00001100, 0b00000000, # /
    0b00001100, 0b00111111, # 0
    0b00000000, 0b00000110, # 1
    0b00000000, 0b11011011, # 2
    0b00000000, 0b10001111, # 3
    0b00000000, 0b11100110, # 4
    0b00100000, 0b01101001, # 5
    0b00000000, 0b11111101, # 6
    0b00000000, 0b00000111, # 7
    0b00000000, 0b11111111, # 8
    0b00000000, 0b11101111, # 9
    0b00010010, 0b00000000, # :
    0b00001010, 0b00000000, # ;
    0b00100100, 0b01000000, # <
    0b00000000, 0b11001000, # =
    0b00001001, 0b10000000, # >
    0b01100000, 0b10100011, # ?
    0b00000010, 0b10111011, # @
    0b00000000, 0b11110111, # A
    0b00010010, 0b10001111, # B
    0b00000000, 0b00111001, # C
    0b00010010, 0b00001111, # D
    0b00000000, 0b11111001, # E
    0b00000000, 0b01110001, # F
    0b00000000, 0b10111101, # G
    0b00000000, 0b11110110, # H
    0b00010010, 0b00000000, # I
    0b00000000, 0b00011110, # J
    0b00100100, 0b01110000, # K
    0b00000000, 0b00111000, # L
    0b00000101, 0b00110110, # M
    0b00100001, 0b00110110, # N
    0b00000000, 0b00111111, # O
    0b00000000, 0b11110011, # P
    0b00100000, 0b00111111, # Q
    0b00100000, 0b11110011, # R
    0b00000000, 0b11101101, # S
    0b00010010, 0b00000001, # T
    0b00000000, 0b00111110, # U
    0b00001100, 0b00110000, # V
    0b00101000, 0b00110110, # W
    0b00101101, 0b00000000, # X
    0b00010101, 0b00000000, # Y
    0b00001100, 0b00001001, # Z
    0b00000000, 0b00111001, # [
    0b00100001, 0b00000000, # \
    0b00000000, 0b00001111, # ]
    0b00001100, 0b00000011, # ^
    0b00000000, 0b00001000, # _
    0b00000001, 0b00000000, # `
    0b00010000, 0b01011000, # a
    0b00100000, 0b01111000, # b
    0b00000000, 0b11011000, # c
    0b00001000, 0b10001110, # d
    0b00001000, 0b01011000, # e
    0b00000000, 0b01110001, # f
    0b00000100, 0b10001110, # g
    0b00010000, 0b01110000, # h
    0b00010000, 0b00000000, # i
    0b00000000, 0b00001110, # j
    0b00110110, 0b00000000, # k
    0b00000000, 0b00110000, # l
    0b00010000, 0b11010100, # m
    0b00010000, 0b01010000, # n
    0b00000000, 0b11011100, # o
    0b00000001, 0b01110000, # p
    0b00000100, 0b10000110, # q
    0b00000000, 0b01010000, # r
    0b00100000, 0b10001000, # s
    0b00000000, 0b01111000, # t
    0b00000000, 0b00011100, # u
    0b00100000, 0b00000100, # v
    0b00101000, 0b00010100, # w
    0b00101000, 0b11000000, # x
    0b00100000, 0b00001100, # y
    0b00001000, 0b01001000, # z
    0b00001001, 0b01001001, # {
    0b00010010, 0b00000000, # |
    0b00100100, 0b10001001, # }
    0b00000101, 0b00100000, # ~
    0b00111111, 0b11111111,
)
NUMBERS = (
    0x3F, # 0
    0x06, # 1
    0x5B, # 2
    0x4F, # 3
    0x66, # 4
    0x6D, # 5
    0x7D, # 6
    0x07, # 7
    0x7F, # 8
    0x6F, # 9
    0x77, # a
    0x7C, # b
    0x39, # C
    0x5E, # d
    0x79, # E
    0x71, # F
    0x40, # -
)

class Seg14x8(HT16K33):
    """Alpha-numeric, 8 character, 14 segment display."""
    def print(self, value):
        """Print the value to the display."""
        if isinstance(value, (str)):
            self._text(value)
        elif isinstance(value, (int, float)):
            self._number(value)
        else:
            raise ValueError('Unsupported display value type: {}'.format(type(value)))
        if self._auto_write:
            self.show()

    def __setitem__(self, key, value):
        self._put(value, key)
        if self._auto_write:
            self.show()

    def scroll(self, count=1):
        """Scroll the display by specified number of places."""
        if count >= 0:
            offset = 0
        else:
            offset = 2
        for i in range(14):
            self._set_buffer(i + offset, self._get_buffer(i + 2 * count))

    def _put(self, char, index=0):
        """Put a character at the specified place."""
        if not 0 <= index <= 7:
            return
        if not 32 <= ord(char) <= 127:
            return
        if char == '.':
            self._set_buffer(index * 2 + 1, self._get_buffer(index * 2 + 1) | 0b01000000)
            return
        character = ord(char) * 2 - 64
        self._set_buffer(index * 2, CHARS[1 + character])
        self._set_buffer(index * 2 + 1, CHARS[character])

    def _push(self, char):
        """Scroll the display and add a character at the end."""
        if char != '.' or self._get_buffer(7) & 0b01000000:
            self.scroll()
            self._put(' ', 7)
        self._put(char, 7)

    def _text(self, text):
        """Display the specified text."""
        for character in text:
            self._push(character)

    def _number(self, number):
        """Display the specified decimal number."""
        auto_write = self._auto_write
        self._auto_write = False
        string = "{}".format(number)
        if len(string) > 8:
            if string.find('.') > 8:
                raise ValueError("Overflow")
        self.fill(False)
        places = 8
        if '.' in string:
            places += 1
        self._text(string[:places])
        self._auto_write = auto_write
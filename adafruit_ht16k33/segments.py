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


class Seg14x4(HT16K33):
    def scroll(self, count=1):
        if count >= 0:
            offset = 0
        else:
            offset = 2
        for i in range(6):
            self._set_buffer(i + offset, self._get_buffer(i + 2 * count))

    def put(self, char, index=0):
        if not 0 <= index <= 3:
            return
        if not 32 <= ord(char) <= 127:
            return
        if char == '.':
            self._set_buffer(index * 2 + 1, self._get_buffer(index * 2 + 1) | 0b01000000)
            return
        c = ord(char) * 2 - 64
        self._set_buffer(index * 2, CHARS[1 + c])
        self._set_buffer(index * 2 + 1, CHARS[c])

    def push(self, char):
        if char != '.' or self._get_buffer(7) & 0b01000000:
            self.scroll()
            self.put(' ', 3)
        self.put(char, 3)

    def text(self, text):
        for c in text:
            self.push(c)

    def number(self, number):
        s = "{:f}".format(number)
        if len(s) > 4:
            if s.find('.') > 4:
                raise ValueError("Overflow")
        self.fill(False)
        places = 4
        if '.' in s:
            places += 1
        self.text(s[:places])

    def hex(self, number):
        s = "{:x}".format(number)
        if len(s) > 4:
            raise ValueError("Overflow")
        self.fill(False)
        self.text(s)


class Seg7x4(Seg14x4):
    P = [0, 2, 6, 8] #  The positions of characters.

    def scroll(self, count=1):
        if count >= 0:
            offset = 0
        else:
            offset = 1
        for i in range(3):
            self._set_buffer(self.P[i + offset], self._get_buffer(self.P[i + count]))

    def push(self, char):
        if char in ':;':
            self.put(char)
        else:
            super().push(char)

    def put(self, char, index=0):
        if not 0 <= index <= 3:
            return
        char = char.lower()
        index = self.P[index]
        if char == '.':
            self._set_buffer(index, self._get_buffer(index) | 0b10000000)
            return
        elif char in 'abcdef':
            c = ord(char) - 97 + 10
        elif char == '-':
            c = 16
        elif char in '0123456789':
            c = ord(char) - 48
        elif char == ' ':
            c = 0x00
        elif char == ':':
            self._set_buffer(4, 0x02)
            return
        elif char == ';':
            self._set_buffer(4, 0x00)
            return
        else:
            return
        self._set_buffer(index, NUMBERS[c])

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT


"""
`adafruit_ht16k33.animations`
==============================

* Authors: ladyada

Test script for display animations on an HT16K33 with alphanumeric display

The display must be initialized with auto_write=False.

"""

from time import sleep

N = 16384
M = 8192
L = 4096
K = 2048
J = 1024
I = 512
H = 256
G2 = 128
G1 = 64
F = 32
E = 16
D = 8
C = 4
B = 2
A = 1


# pylint: disable=invalid-name


class Animation:
    """Animation class for the htk33
    Main driver for all alphanumeric display animations (WIP!!!)

    :param display: HTK33 Display object


    """

    def __init__(self, display):

        self._display = display

    def animate(self, digits, bitmasks, delay=0.2, auto_write=True):
        """Animate function


        :param digits: a list of the digits to write to, in order, like [0, 1, 3]. The digits are
         0 to 3 starting at the left most digit.
        :param bitmasks: a list of the bitmasks to write, in sequence, to the specified digits.
        :param delay: The delay, in seconds (or fractions of), between writing bitmasks to a digit.
        :param auto_write: Whether to actually write to the display immediately or not.


        """

        if not isinstance(digits, list):
            raise ValueError("The first parameter MUST be a list!")
        if not isinstance(bitmasks, list):
            raise ValueError("The second parameter MUST be a list!")
        if delay < 0:
            raise ValueError("The delay between frames must be positive!")
        for dig in digits:
            if not 0 <= dig <= 3:
                raise ValueError("Digit value must be an integer in the range: 0-3")

            for bits in bitmasks:
                if not 0 <= bits <= 0xFFFF:
                    raise ValueError(
                        "Bitmask value must be an integer in the range: 0-65535"
                    )

                self._display.set_digit_raw(dig, bits)

                if auto_write:
                    self._display.show()
                    sleep(delay)

    def chase_forward_and_reverse(self, delay=0.2, cycles=5):
        """Chase Forward and Reverse Animation"""

        cy = 0

        while cy < cycles:
            self.animate([0, 1, 2, 3], [A, 0], delay)
            self.animate([3], [B, C, D, 0], delay)
            self.animate([2, 1, 0], [D, 0], delay)
            self.animate([0], [E, F, H, G2, 0], delay)
            self.animate([1, 2], [G1, G2, 0], delay)
            self.animate([3], [G1, J, A, 0], delay)
            self.animate([2, 1], [A, 0], delay)
            self.animate([0], [A, F, E, D, 0], delay)
            self.animate([1, 2], [D, 0], delay)
            self.animate([3], [D, C, B, J, G1, 0], delay)
            self.animate([2, 1], [G2, G1, 0], delay)
            self.animate([0], [H, 0], delay)

            cy += 1

    def prelude_to_spinners(self, delay=0.2, cycles=5):
        """Prelude to Spinners Animation"""

        cy = 0
        auto_write = False

        while cy < cycles:
            self.animate([1, 2], [A], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0, 3], [A], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [A + F], 0, auto_write)
            self.animate([3], [A + B], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [A + E + F], 0, auto_write)
            self.animate([3], [A + B + C], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [A + D + E + F], 0, auto_write)
            self.animate([3], [A + B + C + D], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([1], [A + D], 0, auto_write)
            self.animate([2], [A + D], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([1], [A + D + M], 0, auto_write)
            self.animate([2], [A + D + K], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([1], [A + D + M + H], 0, auto_write)
            self.animate([2], [A + D + K + J], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [A + E + F + J + D], 0, auto_write)
            self.animate([3], [A + B + C + H + D], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [A + E + F + J + K + D], 0, auto_write)
            self.animate([3], [A + B + C + H + M + D], 0, auto_write)
            self._display.show()
            sleep(delay)

            self._display.fill(0)
            self._display.show()
            sleep(delay)

            cy += 1

    def spinners(self, delay=0.2, cycles=5):
        """Spinners Animation"""

        cy = 0
        auto_write = False

        while cy < cycles:
            self.animate([0], [H + M], 0, auto_write)
            self.animate([1], [J + K], 0, auto_write)
            self.animate([2], [H + M], 0, auto_write)
            self.animate([3], [J + K], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [G1 + G2], 0, auto_write)
            self.animate([1], [G1 + G2], 0, auto_write)
            self.animate([2], [G1 + G2], 0, auto_write)
            self.animate([3], [G1 + G2], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [J + K], 0, auto_write)
            self.animate([1], [H + M], 0, auto_write)
            self.animate([2], [J + K], 0, auto_write)
            self.animate([3], [H + M], 0, auto_write)
            self._display.show()
            sleep(delay)

            cy += 1

        self._display.fill(0)

    def enclosed_spinners(self, delay=0.2, cycles=5):
        """Enclosed Spinner Animation"""
        cy = 0
        auto_write = False

        while cy < cycles:
            self.animate([0], [A + D + E + F + H + M], 0, auto_write)
            self.animate([1], [A + D + J + K], 0, auto_write)
            self.animate([2], [A + D + H + M], 0, auto_write)
            self.animate([3], [A + B + C + D + J + K], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [A + D + E + F + G1 + G2], 0, auto_write)
            self.animate([1], [A + D + G1 + G2], 0, auto_write)
            self.animate([2], [A + D + G1 + G2], 0, auto_write)
            self.animate([3], [A + B + C + D + G1 + G2], 0, auto_write)
            self._display.show()
            sleep(delay)

            self.animate([0], [A + D + E + F + J + K], 0, auto_write)
            self.animate([1], [A + D + H + M], 0, auto_write)
            self.animate([2], [A + D + J + K], 0, auto_write)
            self.animate([3], [A + B + C + D + H + M], 0, auto_write)
            self._display.show()
            sleep(delay)

            cy += 1

        self._display.fill(0)

    def count_down(self):
        """Countdown Method"""
        auto_write = False
        numbers = [
            [A + B + C + D + G1 + G2 + N],
            [A + B + D + E + G1 + G2 + N],
            [B + C + N],
        ]
        index = 0

        self._display.fill(0)

        while index < len(numbers):
            self.animate([index], numbers[index], 0, auto_write)
            self._display.show()
            sleep(1)
            self._display.fill(0)
            sleep(0.5)

            index += 1

        sleep(1)
        self._display.fill(0)

# SPDX-FileCopyrightText: Radomir Dopieralski 2016  for Adafruit Industries
# SPDX-FileCopyrightText: Tony DiCola 2016 for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Drive Multiple Segment Displays
================================
"""
from time import sleep


class Multiple14x4:
    """Class to try and drive multiples of Alpha-numeric, 14-segment displays."""

    def __init__(self, items=None, auto_write=True, brightness=1.0):
        self._auto_write = auto_write
        self._char_count = 0
        if items:
            self._items = items
            for item in self._items:
                self._char_count += item._char_count
        else:
            raise ValueError("Please pass a display")
        self.brightness = brightness
        if self._auto_write:
            self.show()

    def _push(self, char):
        last_display = self._items[len(self._items) - 1]
        if char != "." or last_display.is_last_decimal_set():
            for index, item in enumerate(self._items, start=1):
                if index < len(self._items):
                    item.print_raw(self._items[index].get_raw(0))
                else:
                    item.print(char)
        else:
            last_display.print(char)

    @property
    def blink_rate(self):
        """The blink rate. Range 0-3."""
        return self._items[0].blink_rate

    @blink_rate.setter
    def blink_rate(self, rate=None):
        for item in self._items:
            item.blink_rate = rate

    @property
    def brightness(self):
        """The brightness. Range 0.0-1.0"""
        return self._items[0].brightness

    @brightness.setter
    def brightness(self, brightness):
        for item in self._items:
            item.brightness = brightness

    @property
    def auto_write(self):
        """Auto write updates to the display."""
        return self._items[0].auto_write

    @auto_write.setter
    def auto_write(self, auto_write):
        for item in self._items:
            item.auto_write = auto_write

    def show(self):
        """Refresh the displays and show the changes."""
        for item in self._items:
            item.show()

    def fill(self, color):
        """Fill the displays with the given color"""
        for item in self._items:
            item.fill(color)

    # Just print strings for now, lifted from Seg14x4
    def print(self, value, decimal=0):
        """Print the value to the display."""
        if isinstance(value, (str)):
            self._text(value)
        # elif isinstance(value, (int, float)):
        #    self._number(value, decimal)
        else:
            raise ValueError("Unsupported display value type: {}".format(type(value)))
        if self._auto_write:
            self.show()

    # following functions are lifted from the Seg14x4 class with no change

    def _text(self, text):
        """Display the specified text."""
        for character in text:
            self._push(character)

    def marquee(self, text, delay=0.25, loop=True):
        """
        Automatically scroll the text at the specified delay between characters

        :param str text: The text to display
        :param float delay: (optional) The delay in seconds to pause before scrolling
                            to the next character (default=0.25)
        :param bool loop: (optional) Whether to endlessly loop the text (default=True)

        """
        if isinstance(text, str):
            self.fill(False)
            if loop:
                while True:
                    self._scroll_marquee(text, delay)
            else:
                self._scroll_marquee(text, delay)

    def _scroll_marquee(self, text, delay):
        """Scroll through the text string once using the delay"""
        char_is_dot = False
        for character in text:
            self.print(character)
            # Add delay if character is not a dot or more than 2 in a row
            if character != "." or char_is_dot:
                sleep(delay)
            char_is_dot = character == "."
            self.show()

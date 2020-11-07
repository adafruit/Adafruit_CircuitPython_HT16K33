# The MIT License (MIT)
#
# Copyright (c) 2020 LewsTherinTelamon for Adafruit Industries
# Assistance provided by @madbodger and @KevinThomas on Discord
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



keypad Class for HT16K33. This simple class contains one function that 
uses the parent class "HT16K33"'s i2c_device to write a control code to 
the HT16K33 and then reads back 6 bytes into a bytearray and returns the 
bytearray


"""
from adafruit_ht16k33.ht16k33 import HT16K33

KEYPAD_REGISTER = bytearray([0x40])
READ_BUFFER = bytearray(6)
class keypad(HT16K33):
    
      
    def read_buttons(self):
        

        with self.i2c_device:
            
            self.i2c_device.write_then_readinto(KEYPAD_REGISTER,READ_BUFFER)
        
        return READ_BUFFER


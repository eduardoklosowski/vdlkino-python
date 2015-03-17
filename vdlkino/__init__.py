# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

__version__ = '0.1dev'


HIGH = 1
LOW = 0

INPUT = 0
OUTPUT = 1
INPUT_PULLUP = 2
AUTO = 3


class Vdlkino(object):
    def send_command(self, oper, pin=0, mode=0):
        raise Exception('send_command not implemented')

    def digital_pins(self):
        return self.send_command(0)

    def analog_pins(self):
        return self.send_command(1)

    def set_pin_mode(self, pin, mode):
        return self.send_command(2, pin, mode)

    def get_pin_mode(self, pin):
        return self.send_command(3, pin)

    def set_digital(self, pin, value):
        return self.send_command(4, pin, value)

    def get_digital(self, pin):
        return self.send_command(5, pin)

    def set_analog(self, pin, value):
        return self.send_command(6, pin, value)

    def get_analog(self, pin):
        return self.send_command(7, pin)

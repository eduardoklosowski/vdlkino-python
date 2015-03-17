# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

import serial

from . import Vdlkino


class VdlkinoSerial(Vdlkino):
    def __init__(self, port):
        self.port = port
        self._serial = serial.Serial(port=self.port)

    def send_command(self, oper, pin=0, value=0):
        self._serial.write((oper, pin, value >> 8, value & 0xff))

        ret = self._serial.read(2)
        return (ret[0] << 8) | ret[1]

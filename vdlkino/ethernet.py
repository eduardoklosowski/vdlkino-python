# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from urllib.request import urlopen

from . import Vdlkino


class VdlkinoEthernet(Vdlkino):
    def __init__(self, host, port=80):
        self.host = host
        self.port = port

    def send_command(self, oper, pin=0, value=0):
        with urlopen('http://%s:%d/raw/%d/%d/%d/' % (self.host, self.port,
                                                     oper, pin, value)) as f:
            return int(f.read().decode('ascii'))

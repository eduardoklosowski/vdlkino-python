VDLKino for Python
==================

.. _Arduino: http://arduino.cc/
.. _Python: https://www.python.org/
.. _VDLKino: https://github.com/eduardoklosowski/vdlkino


Library in Python_ for comunicate computer with Arduino_ running VDLKino_.

Support serial (pyserial requirement) and ethernet versions.


Exemple
-------

Blink with Serial comunication
##############################

.. code-block:: python

  from time import sleep
  from vdlkino import HIGH, LOW
  from vdlkino.serial import VdlkinoSerial

  arduino = VdlkinoSerial('/dev/ttyACM0')
  led = 2

  while True:
      arduino.set_digital(led, HIGH)
      sleep(1)
      arduino.set_digital(led, LOW)
      sleep(1)


Blink with Ethernet comunication
################################

.. code-block:: python

  from time import sleep
  from vdlkino import HIGH, LOW
  from vdlkino.ethernet import VdlkinoEthernet

  arduino = VdlkinoEthernet('192.168.1.177')
  led = 2

  while True:
      arduino.set_digital(led, HIGH)
      sleep(1)
      arduino.set_digital(led, LOW)
      sleep(1)

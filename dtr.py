#!/usr/bin/env python                                                                                         
import serial
from time import sleep

dev = '/dev/tty.SLAB_USBtoUART'
baud = 115200
port = serial.Serial(dev, baud)

while 1:
    # setting true outputs 0, setting false outputs 1
    port.setRTS(True)
    port.setDTR(True)
    sleep(1)
    port.setRTS(True)
    port.setDTR(False)
    sleep(1)
    port.setRTS(False)
    port.setDTR(True)
    sleep(1)
    port.setRTS(False)
    port.setDTR(False)
    sleep(1)

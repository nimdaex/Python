#!/usr/bin/env python
import sys, time, os
#from evdev import InputDevice, categorize, ecodes
import serial
from datetime import datetime
now = datetime.now()
print now.strftime('%Y-%m-%d %H:%M:%S')
mySerial = serial.Serial('/dev/ttyS0',9600)
mySerial.write(now.strftime('%Y-%m-%d %H:%M:%S'))

mydata = raw_input('Enter your name:')
print (mydata)
mySerial.write(mydata)
#dev = InputDevice('/dev/input/event0')

#print(dev)
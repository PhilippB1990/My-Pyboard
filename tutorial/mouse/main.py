# main.py -- put your code here!
import pyb
import math

#initialize switch
sw = pyb.Switch()


#LEDS
LEDS = [pyb.LED(i) for i in range(1,5)]
red = pyb.LED(1)
green = pyb.LED(2)
yellow = pyb.LED(3)
blue = pyb.LED(4)


#-------------- mouse -----------------
#
accel = pyb.Accel()
hid = pyb.USB_HID()

while not sw():
    hid.send((0, accel.x(), accel.y(),0))
    pyb.delay(20)

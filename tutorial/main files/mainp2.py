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

'''
# ----------------P2_L2 Fading LEDs --------------
#X resistor in X1-X4, other end into grounding (GND)
#X1 connected to channel 3, Timer 5

#import required frameworks
from pyb import Timer
from time import sleep
#setup timer and channel
timer5 = pyb.Timer(5, freq=100)
tchannel3 = timer5.channel(3, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)

#tim = pyb.Timer(5, freq=100)
#tchannel = tim.channel(3, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)

#Brightness of the LED in PWM is controlled by controlling the pulse-width, 
#that is the amount of time the LED is on every cycle. With a timer frequency of 100 Hz, 
#each cycle takes 0.01 second, or 10 ms.

#set pulse width (equivalent to brightness)
#difference equals brightness change
max_width = 200000
min_width = 10000

#change intensity change per step (10ms)
wstep = 1500
cur_width = min_width

#run changing loop
while not sw():
    tchannel3.pulse_width(cur_width)
    #how often should the pulse_width be called?
    #sleep sets thread to sleep
    sleep(0.001)

    #increase brightness
    cur_width += wstep

    #reset brightness
    #if cur_width > max_width:
    #    cur_width = min_width
    
    #breathing
    if cur_width > max_width:
        cur_width = max_width
        wstep *= -1
    elif cur_width < min_width:
        cur_width = min_width
        wstep *= -1


tchannel3.pulse_width(min_width)
cur_width = min_width       
'''

'''
#  ----------------- P2-1_servo: servo motors
# connection pins: X1, X2, X3, X4
#
servo1 = pyb.Servo(1) #Motor position X1
servo1.angle(90)
def move_motor():
    if servo1.angle() == 85:
        servo1.angle(-85)
    else:
        servo1.angle(95)

sw.callback(move_motor)

#servo1 = pyb.Servo(1)
'''




'''
#---- P1-l9: debounce pin noise ------
def wait_pin_change():
    #wait for pin to change value
    #it needs to be stable for a continous 20ms
    cur_value = pin.value()
    active = 0
    while active < 20:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        pyb.delay(1)



#
pin_x1 = pyb.Pin('X1', pyb.Pin.IN, pyb.Pin.PULL_DOWN)
while True:
    wait_pin_change(pin_x1)
    blue.toggle()
'''




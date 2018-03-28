# main.py -- put your code here! (Part1 - tut 1-7)
import pyb
#import math
#pyb.LED(4).on()

#initialize switch
sw = pyb.Switch()

#LEDS
LEDS = [pyb.LED(i) for i in range(1,5)]
red = pyb.LED(1)
green = pyb.LED(2)
yellow = pyb.LED(3)
blue = pyb.LED(4)

#
#getting switch value -> either sw.value() or sw()
#tell board to do something while switch is pressed: 
# sw.callback(lambda:pyb.LED(1).toggle()) -> lambda function replaces defined function
# or sw.callback(function) 
# -> FUNCTIONS MUST HAVE 0 ARGUMENTS
# -> your functions can not allocate any memory (create variables etc)

# ------------- temporary code ---------------------

'''
def turnOn():
    pyb.LED(4).intensity(255)
def reduceIntensity():
    pyb.LED(4).intensity(50)
def turnOff():
    pyb.LED(4).off()

sw.callback(turnOn)
#sw.callback(reduceIntensity)
#sw.callback(turnOff)
'''

#________________________________ Counters / Timers __________________________
# 14 counters which can have different frequencies (3 reserved, 5&6 used for ADC/DAC)
# timer object tim = pyb.Timer(here timer)
#timer4 = pyb.Timer(4)
#initialize the frequence (herz -> clocks per second)
#timer4.init(freq=10)
#read counter timer4.counter()
#timer4.callback(lambda t:pyb.LED(4).toggle()) #hz/2 - why ever - toggles LED
#to terminate callback -> pass None (timer4.callback(None)

#privded code
#tim4 = pyb.Timer(4, freq=10)
#tim1 = pyb.Timer(1, freq=20)
#tim4.callback(lambda t: pyb.LED(1).toggle())
#tim1.callback(lambda t: pyb.LED(2).toggle())

#microsecond counter
#micros = pyb.Timer(2, prescaler=83, period=0x3fffffff)
#call:start_micros = micros.counter() , reset: micros.counter(0) 
#start_micros = micros.counter()
#-do stuff
#end_micros = micros.counter()

#________________________________ Accelerometer __________________________

#accel = pyb.Accel() # initate object
#values are between -30 and 30
#accel.x()
#accel.y()
#accel.z()

'''
#self written code
accel = pyb.Accel()
lightYellow = pyb.LED(3)
lightBlue = pyb.LED(4)
lightRed = pyb.LED(1)
sensitivity = 10

while True:
    x = accel.x()
    y = accel.y()
    z = accel.z()
    if abs(x) > sensitivity:
        lightYellow.on()
    else:
        lightYellow.off()
    if y > sensitivity:  
        lightBlue.on()
    else:
        lightBlue.off()  
    if z > sensitivity:
        lightRed.on()
    else:
        lightRed.off()

    pyb.delay(10)

#provided code
xlights = (pyb.LED(2), pyb.LED(3))
ylights = (pyb.LED(1), pyb.LED(4))

accel = pyb.Accel()
SENSITIVITY = 3

while True:
    x = accel.x()
    if x > SENSITIVITY: 
        xlights[0].on()
        xlights[1].off()
    elif x < -SENSITIVITY:
        xlights[1].on()
        xlights[0].off()
    else:
        xlights[0].off()
        xlights[1].off()

    y = accel.y()
    if y > SENSITIVITY: 
        ylights[0].on()
        ylights[1].off()
    elif y < -SENSITIVITY:
        ylights[1].on()
        ylights[0].off()
    else:
        ylights[0].off()
        ylights[1].off()

    pyb.delay(100)
'''

'''
# ______________________________ LED disco ______________________________
#create object for each LED | leds[i]
leds = [pyb.LED(i) for i in range(1,5)]
#initiate with resetting LEDs
for l in leds:
    l.off()

#start the disco
n=0 #Laufzeitvariable
try: 
    #while True:
    while sw()==False;
        n = (n+1) % 4
        leds[n].toggle()
        pyb.delay(50) #milliseconds
finally:
    #finalize by resetting leds
    for l in leds:
        l.off()



#The Special LEDs
#----------------

#The yellow and blue LEDs are special. 
# As well as turning them on and off, 
# you can control their intensity using the intensity() method. This takes a number between 0 and 255 that determines how bright it is. The following script makes the blue LED gradually brighter then turns it off again.
#.. code-block:: python
    led = pyb.LED(4)
    intensity = 0
    while True:
        intensity = (intensity + 1) % 255
        led.intensity(intensity)
        pyb.delay(20)
#You can call intensity() on LEDs 1 and 2 but they can only be off or on. 
#0 sets them off and any other number up to 255 turns them on.
'''


# ------ useful functions
# pyb.delay(int value in ms)

#import standards
import pyb
import math

#random number generator
from random import randint

#import sleep
from time import sleep

#import frame buffer
#import framebuf

#import device (w = 128px, h = 160px)
import lcd160cr


#switch object
sw = pyb.Switch()

#lcd object in position X
lcd = lcd160cr.LCD160CR('X')

#create framebuffer (doesn't work)
#fbuf = FrameBuffer(bytearray(10 * 100 * 2), 10, 100, framebuf.RGB565)

#erase currently stored printed values on screen
lcd.erase()

#set LCD position
lcd.set_orient(lcd160cr.PORTRAIT)
lcd.set_pos(0,0)


#main menu interface
def main_touch_interface():
    lcd.erase()
    exit = 0

    fg = lcd.rgb(255, 128, 128)
    bg = lcd.rgb(0, 0, 0)

    #lcd.set_pos(10,10)
    lcd.set_pen(fg, lcd.rgb(128,128,128))
    lcd.rect(5, 5, 116, 150)    
    lcd.set_pos(40,60)
    lcd.write('EXIT')


    while exit == 0:
        lcd.set_power(0)
        t,x,y = lcd.get_touch()
        lcd.set_pos(15,150)
        lcd.write(str(t))
        lcd.set_pos(45,150)
        lcd.write('   ')
        lcd.set_pos(45,150)
        lcd.write(str(x))
        lcd.set_pos(75,150)
        lcd.write('   ')
        lcd.set_pos(75,150)
        lcd.write(str(y))

        if (x > 10 and x < 110 and y > 10 and y < 150):
            exit = 1


# writes log file
def write_log():
    lcd.erase()
    


while not sw():
    lcd.set_pos(60,70)
    lcd.write('NEW ROUTINE')
    pyb.delay(1500)

    lcd.erase()
    main_touch_interface()
    
lcd.erase()
lcd.set_pos(60,70)
lcd.write('TEST FINISHED')
pyb.delay(5000)
lcd.set_power(0)
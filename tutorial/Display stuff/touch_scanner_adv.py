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


#set LCD drawing color
lcd.set_text_color(lcd.rgb(255, 0, 0), lcd.rgb(0, 0, 0))
lcd.set_font(1)


#set special font
#LCD160CR.set_font(font, scale=0, bold=0, trans=0, scroll=0)
#font-families: value 0-3 (3 is huuuuge)
#scale: size -> 0-63
#bold: 0-4 for vertikal direction, 5+ increase boldness
#trans: 0 | 1 -> without or with trans background
#scroll: 0 | 1
#lcd.set_font(1,1,0,0,1)


def touch_pos():
    #local switch
    #screen_sw = pyb.Switch()
    #initiate values
    #lcd.set_text_color(lcd.rgb(255, 0, 0), lcd.rgb(0, 0, 0))
    #
    lcd.erase()
    #t,x,y = lcd.get_touch()
    exit = 0


    #draw squares
    fg = lcd.rgb(255, 128, 128)
    bg = lcd.rgb(0, 0, 0)
    lcd.set_pen(fg, bg)
    #rect(x,y,w,h)
    lcd.rect(2, 2, 50, 80)
    lcd.set_pos(5,5)
    lcd.write('S 1')
    pyb.delay(500)

    lcd.set_pen(fg, lcd.rgb(128,128,128))
    lcd.rect(2, 82, 50, 78)    
    lcd.set_pos(5,85)
    lcd.write('S 2')
    pyb.delay(500)

    lcd.set_pen(fg, lcd.rgb(96,96,96))
    lcd.rect(53, 2, 50, 80)
    lcd.set_pos(56,5)
    lcd.write('S 3')
    pyb.delay(500)

    lcd.set_pen(fg, lcd.rgb(64,64,64))
    lcd.rect(53, 82, 50, 78)
    lcd.set_pos(56,85)
    lcd.write('S 4')

    lcd.set_pen(fg, lcd.rgb(128,0,0))
    lcd.rect(105, 2, 15, 160)
    lcd.set_pos(106,5)
    lcd.write('exit')

    pyb.delay(2000)

    
    while exit==0:
        
        #lcd.erase()
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

        lcd.set_pos(105,150)
        if (x>105):
            exit = 1
        if (x<53 and y<82):
            lcd.write('S1')
        if (x<53 and y>82):
            lcd.write('S2')
        if (x>53 and y<82):
            lcd.write('S3')
        if (x>53 and y>82):
            lcd.write('S4')

        #sleep(1) # pyboard also doesn't recognize input
        pyb.delay(1000) #alternative   
    lcd.erase()
    lcd.set_pos(20,80)
    lcd.write('EXIT TOUCH TEST')

    pyb.delay(3000)

def main(): # call by typing "main()" in console
    lcd.set_pos(0,80)
    lcd.set_text_color(lcd.rgb(255, 0, 0), lcd.rgb(0, 0, 0))
    lcd.erase()
    lcd.write('touch sensor test')
    #pyb.delay(2000)
    #lcd.touch_config(1) //calibration
    pyb.delay(2000)
    touch_pos()
    lcd.erase()
    
    

sw.callback(main) # overrules the other switch

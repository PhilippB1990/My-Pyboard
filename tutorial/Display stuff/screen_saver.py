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
#sw = pyb.Switch()

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

def print_kirby():
    #local switch
    kirby_sw = pyb.Switch()
    #set writing position continousely
    c_x = 0
    c_y = 50
    lcd.set_pos(c_x,c_y)

    while not kirby_sw():
        lcd.set_pos(c_x,c_y)
        lcd.write('<(^^)>')
        c_y += 10
        
        #sleep(1) # pyboard also doesn't recognize input
        pyb.delay(1000) #alternative

def screen_saver():
    #local switch
    screen_sw = pyb.Switch()

    #initiate values
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    cycle = 0

    while not screen_sw():
        if cycle%50==0: 
            lcd.erase()
        #set color random color
        fg = lcd.rgb(randint(128, 255), randint(128, 255), randint(128, 255))
        bg = lcd.rgb(randint(0, 128), randint(0, 128), randint(0, 128))
        lcd.set_pen(fg, bg)
        #randomize values
        x1 = randint(0,lcd.w)
        y1 = randint(0,lcd.h)
        x2 = randint(0,lcd.w)
        y2 = randint(0,lcd.h)
        #draw line (.line if you don't know if inside display, .line_no_clip if certain)
        lcd.line_no_clip(x1,y1,x2,y2)
        
        #sleep(1) # pyboard also doesn't recognize input
        pyb.delay(1000) #alternative
        cycle += 1

def screen_saver_touch():
    #local switch
    screen_sw = pyb.Switch()
    lcd.write('TEST')
    #initiate values
    #lcd.set_text_color(lcd.rgb(255, 0, 0), lcd.rgb(0, 0, 0))
    #
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    cycle = 0
    #touch = 0
    fg = lcd.rgb(255,255,255)
    bg = lcd.rgb(0,0,0)

    while not screen_sw():
        if cycle%50==0: 
            lcd.erase()
        
        if not lcd.is_touched():
            #set lines to green
            fg = lcd.rgb(255,0,0)
            #background black
            bg = lcd.rgb(0,0,0)
        if lcd.is_touched():
            #set lines to something else
            fg = lcd.rgb(0,255,0)
            #background white
            bg = lcd.rgb(128,128,128)
        
        lcd.set_pen(fg, bg)
        x1 = randint(0,lcd.w)
        y1 = randint(0,lcd.h)
        x2 = randint(0,lcd.w)
        y2 = randint(0,lcd.h)
        #draw line (.line if you don't know if inside display, .line_no_clip if certain)
        lcd.line_no_clip(x1,y1,x2,y2)
        
        #sleep(1) # pyboard also doesn't recognize input
        pyb.delay(100) #alternative
        cycle += 1

def main(): # call by typing "main()" in console
    lcd.set_pos(0,80)
    lcd.erase()
    lcd.write('Initate screensaver...')
    pyb.delay(3000)
    screen_saver()
    lcd.erase()
    pyb.delay(3000)
    lcd.set_pos(0,80)
    lcd.write('Screensaver touch...')
    pyb.delay(3000)
    screen_saver_touch()
    lcd.erase()
    

    

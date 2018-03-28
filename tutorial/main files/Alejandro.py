#import standards
import pyb
import math

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

#
brightness = 0
#lcd.set_startup_deco(1)

#
'''
while not sw():
    lcd.set_brightness(brightness)
    brightness = brightness +1
    lcd.write('<(^^)>')
    lcd.write('\n')
    sleep(0.1)
    if brightness==31:
        brightness=0
'''

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
    c_y = 0
    lcd.set_pos(c_x,c_y)

    while not kirby_sw():
        lcd.set_pos(c_x,c_y)
        lcd.write('<(^^)>')
        c_y += 10
        
        #sleep(1) # pyboard also doesn't recognize input
        pyb.delay(1000) #alternative



def main(): # call by typing "main()" in console
    lcd.write('We will now call the kirbies!')
    lcd.set_pos(0,10)
    lcd.write('press USR switch to finish')
    pyb.delay(1000)
    lcd.set_pos(0,20)
    lcd.write('Ready....')
    pyb.delay(2000)
    lcd.set_pos(0,30)
    lcd.write('Steady....')
    pyb.delay(3000)
    lcd.set_pos(0,40)
    lcd.write('GO GO GO')
    pyb.delay(1000)
    print_kirby()

    

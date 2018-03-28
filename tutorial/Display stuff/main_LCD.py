# main.py -- put your code here!
import pyb
import math

#initialize switch
sw = pyb.Switch()


#-------------------------- LCD ----------------------------

#TESTING
#import lcd160cr_test
#lcd160cr_test.test_all('X')


#####
import lcd160cr

#lcd object
lcd = lcd160cr.LCD160CR('X') #sets display to X position (there is just XandY)

#---- simple line -----
#set drawin color (red,green,blue) , set display background
#lcd.set_pen(lcd.rgb(255, 0, 0), lcd.rgb(64, 64, 128))
#draw line with current color
#lcd.line(10,10,50,80)
#lcd.erase()

#---- random rectangles ----
'''
from random import randint
for i in range(1000):
    fg = lcd.rgb(randint(128, 255), randint(128, 255), randint(128, 255))
    bg = lcd.rgb(randint(0, 128), randint(0, 128), randint(0, 128))
    lcd.set_pen(fg, bg)
    lcd.rect(randint(0, lcd.w), randint(0, lcd.h), randint(10, 40), randint(10, 40))
'''
#**Task:** How would you draw two rectangles on the screen? Try to give them different colours.

#---- Redirecting Micropython output to display (Terminal)----
#create UART object (Universal asynchronous receiver-transmitter)
uart_obj = pyb.UART('XA', 115200) #XA -> position again, 115200 is the COM port
#send REPL output to display
pyb.repl_uart(uart_obj)

#?????
#You can adjust the UART baudrate from the default of 115200 using the
#`set_uart_baudrate` method.


#remove current displayed content
#lcd.erase()

# from here http://docs.micropython.org/en/latest/pyboard/library/lcd160cr.html#module-lcd160cr
#lcd = lcd160cr.LCD160CR('X')
#lcd.set_orient(lcd160cr.PORTRAIT)
#lcd.set_pos(0, 0)
#lcd.set_text_color(lcd.rgb(255, 0, 0), lcd.rgb(0, 0, 0))
#lcd.set_font(1)
#lcd.write('Hello MicroPython!')
#print('touch:', lcd.get_touch())



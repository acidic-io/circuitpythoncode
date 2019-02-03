# my fun little neopixel effects library
# acidic.io Feb2019
# you need to have a blank __init__.py file in same directory as fx.py
# call by using 'from fx import *' or import individual functions in code.py or main.py
# pass in num_pixels + pixels for functions to work.
# code.py::: 
# from fx import *
# pixel_pin = board.D12
# num_pixels = 150   # 5m reel of 30 pixel spacing
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
# fxsetup(num_pixels, pixels)
# [then call functions]
# scanline(0)
# fade_up(time, color)

import random
import microcontroller
import time

RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

def fxsetup(num, pix):
    global num_pixels
    global pixels
    num_pixels = num
    pixels = pix

def fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def scanline(wait):
    pixels.fill((0, 0, 0))
    pixels.show()
    for i in range(num_pixels):
        pixels[i] = (0, 255, 255)
        pixels[(i-1)] = (0, 0, 0)
        pixels._brightness = 1
        pixels.show()
     #     print(i, "is on")
        # 89 is ON
    for x in range(1, num_pixels):
        # i has value of 89
    #    print((1+(i-x)), "is off and", i-x, "is on and x is", x)
        pixels[i] = (0, 0, 0)
        # 89 is off
        pixels[(i-x)] = (0, 255, 255)
        pixels[(1+(i-x))] = (0, 0, 0)
        # 89-1, 88 is on
        pixels._brightness = 1
        pixels.show()

def scanlines(wait):
    pixels.fill((0, 0, 0))
    pixels.show()
    for i in range((num_pixels-9)):
        pixels[i] = (0, 255, 255)
        pixels[i+1] = (0, 255, 255)
        pixels[i+2] = (0, 255, 255)
        pixels[i+3] = (0, 255, 255)
        pixels[i+4] = (0, 255, 255)
        pixels[i+5] = (0, 255, 255)
        pixels[i+6] = (0, 255, 255)
        pixels[i+7] = (0, 255, 255)
        pixels[i+8] = (0, 255, 255)
        pixels[i+9] = (0, 255, 255)
        pixels[(i-1)] = (0, 0, 0)
        pixels._brightness = 1
        pixels.show()
def pulser(wait):
    for t in range(10):
        pixels.fill((100, 100, 255))
        pixels.show()
        time.sleep(wait)
        pixels.fill((50, 100, 255))
        pixels.show()
        time.sleep(wait)
        pixels.fill((0, 100, 255))
        pixels.show()   
        time.sleep(wait)
        pixels.fill((0, 50, 255))
        pixels.show()  
        time.sleep(wait)
# this will begin at 0.1 and increase to 0.50
def fade_up(wait, color):
    pixels.fill(color)
    b = 0.03
    time.sleep(wait)   # just a pause
    for ib in range(0, 60):
        b = b+0.01
        pixels._brightness = (b)
        pixels.show()
    #   print(pixels.brightness)
        time.sleep(wait)

def fade_down(wait):
    b = 0.7
    for db in range(1, 67):
        b = b-0.01
        pixels._brightness = (b)
        pixels.show()
    #    print(pixels.brightness)
        time.sleep(wait)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            colors = wheel(rc_index & 255)
            pixels[i] = colors
        pixels.show()
        time.sleep(wait)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
        
def rand(maxtimes, color):
    for x in range(maxtimes):     # goes through x100
        rnum = random.randint(0, (num_pixels-1))
       # print(rnum)
        pixels[rnum] = (color)
        pixels.show()
        # track rnum, incase there is dupes
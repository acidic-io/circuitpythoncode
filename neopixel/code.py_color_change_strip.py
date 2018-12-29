# 5M Reel of neopixel, 30 per M spacing.
# Xmas Tree strip effects.
# acidic.io Dec2019

import time
import board
import neopixel

pixel_pin = board.D12
num_pixels = 150   # 5m reel of 30 pixel spacing
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

def scanline(wait):
    pixels.fill((0, 0, 0))
    pixels.show()
    for i in range(num_pixels):
        pixels[i] = (0, 255, 255)
        pixels[(i-1)] = (0, 0, 0)
        pixels._brightness = 1
        pixels.show()
     #   time.sleep(0.0001)
        print(i, "is on")
        # 89 is ON
    for x in range(1, num_pixels):
        # i has value of 89
        print((1+(i-x)), "is off and", i-x, "is on and x is", x)
        pixels[i] = (0, 0, 0)
        # 89 is off
        pixels[(i-x)] = (0, 255, 255)
        pixels[(1+(i-x))] = (0, 0, 0)
        # 89-1, 88 is on
        pixels._brightness = 1
        pixels.show()
     #    time.sleep(0.0001)


# this will begin at 0.1 and increase to 0.50
def fade_up(wait, color):
    pixels.fill(color)
    b = 0.03
    time.sleep(wait)   # just a pause
    for ib in range(0, 60):
        b = b+0.01
        pixels._brightness = (b)
        pixels.show()
        print(pixels.brightness)
        time.sleep(wait)

def fade_down(wait):
    b = 0.7
    for db in range(1, 67):
        b = b-0.01
        pixels._brightness = (b)
        pixels.show()
        print(pixels.brightness)
        time.sleep(wait)
        
while True: 
        fade_up(0.01, RED)
        fade_down(0.01)
        fade_up(0.01, GREEN)
        fade_down(0.01)
        fade_up(0.01, PURPLE)
        fade_down(0.01)
        fade_up(0.01, CYAN)
        fade_down(0.01)
        fade_up(0.01, PURPLE)
        fade_down(0.01)
        fade_up(0.01, BLUE)
        fade_down(0.01)
    #    scanline(0.03)
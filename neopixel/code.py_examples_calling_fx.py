# 5M Reel of neopixel, 30 per M spacing.
# effects are in fx.py
# acidic.io Feb2019

import board
import neopixel
from fx import *

pixel_pin = board.D12
num_pixels = 150   # 5m reel of 30 pixel spacing
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

fxsetup(num_pixels, pixels)

while True: 
        fade_up(0, PURPLE)
        rand(150, CYAN)
        fade_down(0)
        fade_up(0, CYAN)
        rand(150, PURPLE)
        fade_down(0)
    #    scanline(0.01)
    #   scanlines(0.01)
    #    pulser(0.5)    
    #   rainbow_cycle(0)
    #    rand(10, BLUE)
    #    rand(5, GREEN)
    #   rand(15, OFF)
     #   print("CPU Temp:", fahrenheit(microcontroller.cpu.temperature), "F")
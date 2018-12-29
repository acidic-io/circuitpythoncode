# itsybitsy M4 motion activated lights for stairs.
# acidic.io Dec 2019
import time
import board
import neopixel
import digitalio

# neopixel strip setup
pixel_pin = board.D11
num_pixels = 8   # how many pixels do you have
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

# setup PIR sensor
pir_pin = board.D9
pir = digitalio.DigitalInOut(pir_pin)
pir.direction = digitalio.Direction.INPUT

# neopixel strip effects
def scanline(wait):
    pixels.fill((0, 0, 0))
    pixels.show()
    for i in range(num_pixels):
        pixels[i] = (0, 255, 255)
        pixels[(i-1)] = (0, 0, 0)
        pixels.show()
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
        pixels.show()


# this will begin at 0.1 and increase to 0.70
def fade_up(wait):
    pixels.fill((0, 100, 255))
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
        
# Main loop that will run forever:
old_value = pir.value
while True:
    pir_value = pir.value
    if pir_value:
        # PIR is detecting movement! Turn on strip
        fade_up(0.05)
        fade_down(0.05)
        # Check if this is the first time movement was
        # detected and print a message!
        if not old_value:
            print('Motion detected!')
    else:
        # PIR is not detecting movement. Turn off strip
        pixels.fill((0, 0, 0))  # keep pixels off, conserve energy
        pixels.show()
        # Again check if this is the first time movement
        # stopped and print a message.
        if old_value:
            print('Motion ended!')
    old_value = pir_value
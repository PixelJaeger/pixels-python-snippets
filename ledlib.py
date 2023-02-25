"""
this is a small LED library for use with the neopixel module
invoke via 'from name_of_library.py import specific_funtion'
or 'from name_of_library.py import *'
"""
# importing necessary stuff
import random, board, neopixel
from time import sleep

# LED variables
# as long as invoke with:
# "with neopixel.NeoPixel(board.D21, 16) as pixels:"
# following lines are not needed
# pixel_pin = board.D21    # which GPIO-Pin is used
# num_pixels = 16          # how many LEDs are on the neopixel
ORDER = neopixel.RGB       # some neopixel have a different order

# the followinf variable is for the standard run&fill-light. the
# variables are changeable and you can add more colors.
# the format has to stay the same though. ie (0xFF00FF) for pink
COLORS = (0xFF0000, 0xFF007D, 0x7D00FF, 0x0000FF, 0x007DFF, 0x00FF7D, 0x00FF00, 0x7DFF00, 0xFF7D00)
off = (0x000000)

# defined variables
c_wait = 1
short = 0.005
longer = 0.009
r_pos = 0
r_col = 0
g_col = 0
b_col = 0
pos = 0
r = 0
bright = 0.000

# i decided to let the functions stay clustered instead of moving
# them logically. This way you can see which LED-Functions use
# certain needed functions "random position", "random color" and "wait"-ticks)


# pastel colors @ random led's
def rand_pos(r_pos):
  r_pos = random.randrange(0, 16, 1)
  return(r_pos)

def rgb_val(r):
  r = random.randrange(25, 100, 1)
  return(r)

def rnd_pastel():
    for i in range(1, 100, 1):
      pixels.brightness=0.03
      pos = rand_pos(r_pos)
      r_col = rgb_val(r)
      g_col = rgb_val(r)
      b_col = rgb_val(r)
      pixels[pos] = r_col, g_col, b_col
      sleep(0.05)

# hard colors @ random led's
def rnd_color():
    for i in range(1, 25, 1):
      pixels.brightness=0.03
      pos = rand_pos(r_pos)
      pixels[pos] = (255, 0, 0)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (255, 0, 125)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (125, 0, 255)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (0, 0, 255)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (0, 255 ,255)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (0, 255 ,125)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (0, 255 ,0)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (255, 255 ,0)
      sleep(0.05)
      pos = rand_pos(r_pos)
      pixels[pos] = (255, 125 ,0)
      sleep(0.05)

# Knight-Rider Style Lauflicht
def knight():
    for i in range(1, 10, 1):
        ############ Left to Right ##################  
        for x in range(0, 14, 1):
            pixels[x+1] = (255, 0, 0)
            sleep(short)
            pixels[x] = (255, 0, 0)
            sleep(longer)
            pixels[x+1] = (255, 0, 0)
            sleep(longer)
            pixels[x+2] = (255, 0, 0)
            sleep(longer)
            pixels[x] = (0, 0, 0)
            sleep(longer)
            pixels[x+1] = (255, 0, 0)
            sleep(longer)
            pixels[x+2] = (0, 0, 0)
        sleep(0.1)
        ############ Left to Right ##################  
        for x in range(13, 0, -1):
            pixels[x+1] = (255, 0, 0)
            sleep(longer)
            pixels[x] = (255, 0, 0)
            sleep(longer)
            pixels[x+1] = (255, 0, 0)
            sleep(longer)
            pixels[x+2] = (255, 0, 0)
            sleep(longer)
            pixels[x] = (0, 0, 0)
            sleep(longer)
            pixels[x+1] = (255, 0, 0)
            sleep(longer)
            pixels[x+2] = (0, 0, 0)
        sleep(0.5)

# rainbow
num_pixels = 16
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(rain_wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        sleep(rain_wait)

# circle run where led's stay on
def tick(c_wait):
  val = c_wait / 100
  return(val)

def circle_fill():
    for a in range(1, 5, 1):
      for color in COLORS:
        for i in range(num_pixels):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))

    for a in range(5, 1, -1):
      for color in COLORS:
        for i in range(num_pixels):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))

# circle run where led's go off again
def circle_nofill():
    for a in range(1, 5, 1):
      for color in COLORS:
        for i in range(num_pixels):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))
          pixels.fill(0)
    for a in range(5, 1, -1):
      for color in COLORS:
        for i in range(num_pixels):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))
          pixels.fill(0)

# led fill until full and then remove until empty
def circle_fillandclear():
    for a in range(1, 3, 1):
      for color in COLORS:
        for i in range(num_pixels):
          pixels[i] = color
          pixels.show()
          sleep(0.05)
        for i in range(15, 0, -1):
          pixels[i] = off
          pixels.show()
          sleep(0.05)

# led fill until full and then remove until empty
def circle_fillandclear_b():
    for a in range(1, 3, 1):
      for color in COLORS:
        for i in range(num_pixels):
          pixels[i] = color
          pixels.show()
          sleep(0.05)
        for i in range(0, 16, 1):
          pixels[i] = off
          pixels.show()
          sleep(0.05)

# "breathing" brightness on all leds, cycles through colors
def circle_pulse():
      global bright
      pixels.brightness=bright
      for color in COLORS:
        for a in range(0, 25, 1):
          pixels.fill(color)
          bright += 0.004
          pixels.brightness=bright
          sleep(0.05)
        for b in range(25, 0, -1):
          pixels.fill(color)
          bright -= 0.004
          pixels.brightness=bright
          sleep(0.05)

# use "with neopixel.NeoPixel(board.D'PIN', 'LED AMOUNT') as pixels:"
# in order for leds going out after exiting the script. Otherwise they stay on
with neopixel.NeoPixel(board.D21, 16) as pixels:
    pixels.brightness=0.045
    while True:
#        knight()
#        circle_nofill()
        circle_fill()
        circle_fillandclear()
        circle_fillandclear_b()
        rnd_color()
        rnd_pastel()
        rainbow_cycle(0.01)
        circle_pulse()
 

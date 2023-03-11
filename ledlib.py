"""
this is a small LED library for use with the neopixel module
invoke via 'from name_of_library.py import specific_funtion'
or 'from name_of_library.py import *'
"""
# importing necessary stuff
import random, board, neopixel
from time import sleep

# importing for clean closure on reboot/shutdown otherwise
# the LED will stay on until disconnected manually
import sys, signal

# pixel_pin = board.D21    # which GPIO-Pin is used

pixel_count = 16  # Change this to your "LED-Count -1"

ORDER = neopixel.RGB       # some neopixel have a different order

# the followinf variable is for the standard run&fill-light. the
# variables are changeable and you can add more colors.
# the format has to stay the same though. ie (0xFF00FF) for pink
COLORS = (0xFF0000, 0xFF007D, 0x7D00FF, 0x0000FF, 0x007DFF, 0x00FF7D, 0x00FF00, 0x7DFF00, 0xFF7D00)
col_dim= (0x280000, 0x28001A, 0x1A0028, 0x000028, 0x001A28, 0x00281A, 0x002800, 0x1A2800, 0x281A00)
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
orig_bright = 0.045

def rand_pos(r_pos):
  r_pos = random.randrange(0, pixel_count, 1)
  return(r_pos)

def rgb_val(r):
  r = random.randrange(25, 100, 1)
  return(r)

def tick(c_wait):
  val = c_wait / 100
  return(val)


# pastel colors @ random led's
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

# rainbow
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
        for i in range(pixel_count):
            pixel_index = (i * 256 // pixel_count) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        sleep(rain_wait)

# circle run where led's stay on
def circle_fill():
    for a in range(1, 5, 1):
      for color in COLORS:
        for i in range(pixel_count):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))

    for a in range(5, 1, -1):
      for color in COLORS:
        for i in range(pixel_count):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))

# circle run where led's go off again
def circle_nofill():
    for a in range(1, 5, 1):
      for color in COLORS:
        for i in range(pixel_count):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))
          pixels.fill(0)
    for a in range(5, 1, -1):
      for color in COLORS:
        for i in range(pixel_count):
          pixels[i] = color
          pixels.show()
          sleep(tick(a))
          pixels.fill(0)

# led fill until full and then remove until empty
def circle_fillandclear():
    for a in range(1, 3, 1):
      for color in COLORS:
        for i in range(pixel_count):
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
        for i in range(pixel_count):
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
      pixels.brightness=orig_bright

# 4 leds across each other going in a circle
# changing colors each position
def fourpoint():
  global a, b, c, d
  a = -1
  b = 3
  c = 7
  d = 11
  for loop in range(1, 15, 1):
    for color in COLORS:
      a += 1
      b += 1
      c += 1
      d += 1
      if a == 16:
       a -= 16
      if b == 16:
       b -= 16
      if c == 16:
       c -= 16
      if d == 16:
       d -= 16
      pixels[a] = color
      pixels[b] = color
      pixels[c] = color
      pixels[d] = color
      sleep(tick(loop))
      pixels.fill(0)
  for loop in range(15, 1, -1):
    for color in COLORS:
      a += 1
      b += 1
      c += 1
      d += 1
      if a == 16:
       a -= 16
      if b == 16:
       b -= 16
      if c == 16:
       c -= 16
      if d == 16:
       d -= 16
      pixels[a] = color
      pixels[b] = color
      pixels[c] = color
      pixels[d] = color
      sleep(tick(loop))
      pixels.fill(0)

# 2 leds across each other going in a circle
# changing colors each position
def twopoint():
  global a, c
  a = -1
  c = 7
  for loop in range(1, 15, 1):
    for color in COLORS:
      a += 1
      c += 1
      if a == 16:
       a -= 16
      if c == 16:
       c -= 16
      pixels[a] = color
      pixels[c] = color
      sleep(tick(loop))
      pixels.fill(0)
  for loop in range(15, 1, -1):
    for color in COLORS:
      a += 1
      c += 1
      if a == 16:
       a -= 16
      if c == 16:
       c -= 16
      pixels[a] = color
      pixels[c] = color
      sleep(tick(loop))
      pixels.fill(0)

# 2 leds across each other going in a circle
# changing colors each position
def chase():
  global col_dim
  for loop in range(1, 2, 1):
    for color in range(0, 8, 1):
      for i in range(1, 15, 1):
        pixels.fill(0)
        pixels[15] = col_dim[color]
        pixels[0] = COLORS[color]
        pixels[1] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[0] = col_dim[color]
        pixels[1] = COLORS[color]
        pixels[2] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[1] = col_dim[color]
        pixels[2] = COLORS[color]
        pixels[3] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[2] = col_dim[color]
        pixels[3] = COLORS[color]
        pixels[4] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[3] = col_dim[color]
        pixels[4] = COLORS[color]
        pixels[5] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[4] = col_dim[color]
        pixels[5] = COLORS[color]
        pixels[6] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[5] = col_dim[color]
        pixels[6] = COLORS[color]
        pixels[7] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[6] = col_dim[color]
        pixels[7] = COLORS[color]
        pixels[8] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[7] = col_dim[color]
        pixels[8] = COLORS[color]
        pixels[9] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[8] = col_dim[color]
        pixels[9] = COLORS[color]
        pixels[10] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[9] = col_dim[color]
        pixels[10] = COLORS[color]
        pixels[11] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[10] = col_dim[color]
        pixels[11] = COLORS[color]
        pixels[12] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[11] = col_dim[color]
        pixels[12] = COLORS[color]
        pixels[13] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[12] = col_dim[color]
        pixels[13] = COLORS[color]
        pixels[14] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[13] = col_dim[color]
        pixels[14] = COLORS[color]
        pixels[15] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[14] = col_dim[color]
        pixels[15] = COLORS[color]
        pixels[0] = col_dim[color]
        sleep(tick(i))
      for i in range(15, 1, -1):
        pixels.fill(0)
        pixels[15] = col_dim[color]
        pixels[0] = COLORS[color]
        pixels[1] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[0] = col_dim[color]
        pixels[1] = COLORS[color]
        pixels[2] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[1] = col_dim[color]
        pixels[2] = COLORS[color]
        pixels[3] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[2] = col_dim[color]
        pixels[3] = COLORS[color]
        pixels[4] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[3] = col_dim[color]
        pixels[4] = COLORS[color]
        pixels[5] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[4] = col_dim[color]
        pixels[5] = COLORS[color]
        pixels[6] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[5] = col_dim[color]
        pixels[6] = COLORS[color]
        pixels[7] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[6] = col_dim[color]
        pixels[7] = COLORS[color]
        pixels[8] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[7] = col_dim[color]
        pixels[8] = COLORS[color]
        pixels[9] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[8] = col_dim[color]
        pixels[9] = COLORS[color]
        pixels[10] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[9] = col_dim[color]
        pixels[10] = COLORS[color]
        pixels[11] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[10] = col_dim[color]
        pixels[11] = COLORS[color]
        pixels[12] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[11] = col_dim[color]
        pixels[12] = COLORS[color]
        pixels[13] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[12] = col_dim[color]
        pixels[13] = COLORS[color]
        pixels[14] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[13] = col_dim[color]
        pixels[14] = COLORS[color]
        pixels[15] = col_dim[color]
        sleep(tick(i))
        pixels.fill(0)
        pixels[14] = col_dim[color]
        pixels[15] = COLORS[color]
        pixels[0] = col_dim[color]
        sleep(tick(i))



# handler for catching and acting upon shutdown/reboot
pix_empty = neopixel.NeoPixel(board.D21, 16)

def handler(signum = None, frame = None):
    pix_empty.fill(0, 0, 0)
    sleep(1)  #here check if process is done
    print('done')
    sys.exit(0)

# catches reboot/shutdown signal
for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
    signal.signal(sig, handler)

# use "with neopixel.NeoPixel(board.D'PIN', 'LED AMOUNT') as pixels:"
# in order for leds going out after exiting the script. Otherwise they stay on
with neopixel.NeoPixel(board.D21, pixel_count) as pixels:
    pixels.brightness=orig_bright
    while True:


############################################
# comment / uncomment the functions below  #
# depending on your liking                 #
############################################

#        circle_nofill()
        chase()
        twopoint()
        fourpoint()
        circle_fill()
        circle_fillandclear()
        circle_fillandclear_b()
        rnd_color()
        rnd_pastel()
        circle_pulse()
        rainbow_cycle(0.01)

# neopixel-python-demo
this repo is for programming neopixel led-rings and/or led-strips on Python.<br/>
tested on python 3.9.2 and an 16 LED NeoPixel Ring.<br/>
<br/>
<br/>
<br/>
<b>ledlib.py</b><br/>
the main file. it contains all functions needed.<br/>
you can change the led-functions ad the bottom of<br/>
the file to your liking.<br/>
i.e.: change the order of the demos.<br/>
<br/>
<b>led_neopixel_req.txt</b><br/>
lists all the requirements. which as of now is only <br/>
"adafruit-circuitpython-neopixel". <br/>
in the future i might add additional functions that<br/>
might need different modules.<br/>
<br/>
<b>process-kill.py</b><br/>
as mentioned within that file:<br/>
use this if you ran the script automatically @ bootup<br/>
and want/need to kill it. I do not know if it will<br/>
work for you, so use it at your own risk.<br/>
<br/>
<b>nuka_display.py</b><br/>
Temperature and Humidity Displayed on a 7 segment 4 Digit Display-module<br/>
Has also Scrolltext (needs to be uncommented in order to work<br/>
Uses input from a DHT22 Temperature/Humidity Sensor<br/>
<br/>
<b>nuka_led.py</b><br/>
Small LED script for my 5 UV-LED "Nuka Cola Quantum" Bottle<br/>
Uses "Argsparse" for startparameters <br/>
Use "nuka_led.py -h" for more info.<br/>
<br/>



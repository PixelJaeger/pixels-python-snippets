import time
import board
import adafruit_dht
import tm1637
from time import localtime

tm = tm1637.TM1637(clk=26, dio=19)                              # clk and dio need to be changes according to you pin usage
dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio=False)    # "(board.D15) needs to be changed according to your pin usage)
tm.brightness(1)                                                # brightness settings for the LED-Display (0 = off, 7 = staring into the sun)
tm.show('    ')

def clock_time():
    t = localtime()
    tm.numbers(t.tm_hour, t.tm_min)
    time.sleep(1)
    tm.numbers(t.tm_hour, t.tm_min, False)
    time.sleep(1)
    tm.numbers(t.tm_hour, t.tm_min)
    time.sleep(1)
    tm.numbers(t.tm_hour, t.tm_min, False)
    time.sleep(1)
    tm.numbers(t.tm_hour, t.tm_min)
    time.sleep(1)
    tm.numbers(t.tm_hour, t.tm_min, False)
    #time.sleep(1)

def temp_humi():
    global temperature_c
    global humidity
    temperature_c = dhtDevice.temperature               # get temperature from sensor
    humidity = dhtDevice.humidity                       # get humidity from sensor
    tempe = str(temperature_c)                          # convert to string
    humi = str(humidity)
    tempe = tempe[:2]                                   # only use first to characters of string
    humi = humi[:2]
    tempe = tempe+'*C'                                  # append "*C" to string
    #print('temp:',tempe)                               # uncomment for console output of temperature and humidity
    #print('humi',humi)
    tm.show(tempe)                                      # show Temperature-string on LED Display
    time.sleep(3)
    tm.show('    ')                                     # clear LED Display
    tm.write([0, 0 , 0 , 116])                                     
    tm.show(humi)                                       # shot Humidity-String on LED Display
    time.sleep(3)

def scroll_text():
     tm.scroll('Nuka Cola Quantum')

def scroll_temp():
    global temperature_c_s
    global humidity_s
    temperature_c_s = dhtDevice.temperature               # get temperature from sensor
    humidity_s = dhtDevice.humidity                       # get humidity from sensor
    tempe_s = str(temperature_c_s)                          # convert to string
    humi_s = str(humidity_s)
    tempe_s = tempe_s[:2]                                   # only use first to characters of string
    humi_s = humi_s[:2]
    tempe_s = tempe_s+'*C'                                  # append "*C" to string
    scroll_text = tempe_s + '    ' + humi_s + ' h'
    tm.scroll(scroll_text, 500)

while True:
        try:
            temp_humi()
            clock_time()
            scroll_temp()
            clock_time()
            #scroll_text()

        except RuntimeError as error:
            #print(error.args[0])                   #uncomment for error messages in console
            time.sleep(1)
            continue
        except Exception as error:
            #dhtDevice.exit()                       #drops device in case of "big" errors
            #raise error                            #shows "big" errors in the console
            time.sleep(1)
            continue
        time.sleep(1)

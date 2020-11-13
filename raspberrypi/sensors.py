#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_DHT.DHT11
pin = 23

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    
    
    count = 0
  
    #Output on the pin for 
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(7, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(7) == GPIO.LOW):
        count += 1

    #return count    
    
    #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity) + " - " + str(count))
    
    print(json.dumps({'response':'success','data':{'temperature': temperature, 'humidity': humidity, 'light_level': count}}, sort_keys=True, indent=4))
    
else:
    print(json.dumps({'response':'error'}, sort_keys=True, indent=4))
    sys.exit(1)

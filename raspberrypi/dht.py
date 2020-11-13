#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_DHT.DHT11
pin = 23

pin_to_circuit = 7


def rc_time (pin_to_circuit):
    
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    #if humidity is not None and temperature is not None:
        #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    #else:
        #print('Failed to get reading. Try again!')
        #sys.exit(1)
    
    
    
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(2)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return str(count) + " - " + str(temperature) + " - " + str(humidity)





    
#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
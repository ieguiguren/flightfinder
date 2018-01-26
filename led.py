#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import RPi.GPIO as GPIO
except ImportError as e:
    print ("Error: %s \n" % (e))
    print("Are you running this in Raspian?")
    sys.exit(1)

class Led:
    ''' manages easily a Led on raspberry pi'''
    def __init__(self, pin=17):
        #GPIO 17 is board pin 11
        ON = True
        OFF = False
        self.pin = pin
        self.status = OFF
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def ON(self):
        ''' turns the led on '''
        GPIO.output( self.pin, ON)

    def OFF(self):
        ''' turns the led on '''
        GPIO.output( self.pin, OFF)

    def end(self):
        ''' frees the pin '''
        GPIO.cleanup()


def main():
    #changes the state of the led every time <ENTER> is pushed
    led = Led(17)
    while true:
        led.ON()
        raw_input()
        led.OFF()
        raw_input()


if __name__ == "__main__":
    main()


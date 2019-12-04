#!/usr/bin/env python3


import time
import RPi.GPIO as GPIO


lightpin1 = 37
lightpin2 = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightpin1, GPIO.OUT)
GPIO.setup(lightpin2, GPIO.OUT)


while True:
    GPIO.output(lightpin1, True)
    time.sleep(1)
    GPIO.output(lightpin2, True)
    time.sleep(1)

    GPIO.output(lightpin1, False)
    time.sleep(1)
    GPIO.output(lightpin2, False)
    time.sleep(1)


GPIO.cleanup()

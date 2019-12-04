#!/usr/bin/env python3


import time
import RPi.GPIO as GPIO
import datetime
import logging


def light_state(lightpin, state):
    GPIO.output(lightpin, state)
    time.sleep(1)


def off_everything(pins):
    for pin in pins:
        if GPIO.input(pin):
            light_state(pin, False)


logname = '/var/tmp/instalatie.log'
logging.basicConfig(filename=logname, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

lightpin1 = 37
lightpin2 = 26


while True:
    dt = datetime.datetime.now()
    if dt.time() < datetime.time(23) and dt.time() > datetime.time(18):
        if not GPIO.getmode():
            logging.info('Dam drumu\' la instalatie')
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(lightpin1, GPIO.OUT)
            GPIO.setup(lightpin2, GPIO.OUT)

        light_state(lightpin1, True)
        light_state(lightpin2, True)
        
        light_state(lightpin1, False)
        light_state(lightpin2, False)

    else:
        if GPIO.getmode():
            logging.info('Oprim instalatia')
            off_everything([lightpin1, lightpin2])
            GPIO.cleanup()
        else:
            logging.info('Inca nu!')
        time.sleep(1800)


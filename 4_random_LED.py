import RPi.GPIO as GPIO
import time
import random

# board setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led_pins = [8, 10, 12]
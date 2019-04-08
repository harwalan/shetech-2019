import RPi.GPIO as GPIO
import time
import random

# board setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led_pins = [8, 10, 12]

GPIO.setup(8,GPIO.OUT)  #first LED
GPIO.setup(10,GPIO.OUT) # second LED
GPIO.setup(12,GPIO.OUT) # third LED
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button

while True:  
    input_state = GPIO.input(16) 
    if input_state == False:
        print('Button Pressed')
        random_led = random.choice(led_pins)
        GPIO.output(random_led,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(random_led,GPIO.LOW)
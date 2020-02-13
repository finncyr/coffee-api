#import RPi.GPIO as GPIO
from os import uname
import time

def brewCoffee():

    if(uname()[4][:3] == 'arm'):
      #  GPIO.setmode(GPIO.BCM)
      print("This is ARM")
      #  GPIO.setup(23, GPIO.OUT)
      #  GPIO.output(23, GPIO.HIGH)
      #  time.sleep(0.325)
      #  GPIO.output(23. GPIO.LOW) 
    else:
        print("SIMULATED GPIO 23: On")
        time.sleep(0.325)
        print("SIMULATED GPIO 23: Off")



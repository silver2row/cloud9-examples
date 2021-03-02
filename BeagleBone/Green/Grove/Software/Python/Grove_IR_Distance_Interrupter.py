#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import os

IR = "P9_19"

if __name__ == "__main__":
   GPIO.setup(IR, GPIO.IN)

   while True:
      try:
         if GPIO.input(IR) == GPIO.LOW:
             print ("found something")
         else:
            print ("nothing")
         time.sleep(0.5)
      except IOError:
         print ("Error")

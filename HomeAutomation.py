import RPi.GPIO as GPIO
from Distance import DistanceSensor
import time

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

d = DistanceSensor(16, 20)
dis = d.measureDistance()

if dis > 2 and dis < 300:
    print 'alerting owner'
    GPIO.setup(24, GPIO.OUT)
    time.sleep(1)
    GPIO.output(24, GPIO.HIGH)
    GPIO.setup(25, GPIO.OUT)
    time.sleep(1)
    GPIO.output(25, GPIO.HIGH)
    GPIO.setup(8, GPIO.OUT)
    time.sleep(1)
    GPIO.output(8, GPIO.HIGH)
    GPIO.setup(7, GPIO.OUT)
    time.sleep(1)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(7, GPIO.LOW) 


GPIO.cleanup()

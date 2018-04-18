import RPi.GPIO as GPIO
from Distance import DistanceSensor
from Motion import MotionSensor
from TempHum import  TempHumSensor
from Smoke import SmokeSensor
import time
import traceback

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# %%%%%%% distance sensor %%%%%%%%%%%
##d = DistanceSensor(16, 20)
##dis = d.measureDistance()
##
##if dis > 2 and dis < 300:
##    print 'alerting owner'
##    GPIO.setup(7, GPIO.OUT)
##    time.sleep(5)
##    GPIO.output(7, GPIO.HIGH)
##    time.sleep(2)
##    GPIO.output(7, GPIO.LOW) 

# %%%%% motion %%%%%%
##m = MotionSensor(8, 2)
##try:
##    m.detectMotion()
##except:
##    print 'caught exception'
##    traceback.print_exc()
##    GPIO.cleanup()

# %%%%% temperature and humidity %%%%%
##th = TempHumSensor(24, 19)
##try:
##    th.measureTempHum()
##    th.setSignal()
##except:
##    pass

# %%%%%% smoke %%%%%%%%%

s = SmokeSensor(25,26)
try:
    s.detectSmoke()
except:
    print 'ended by Ctrl+C'
    traceback.print_exc()
    GPIO.cleanup()


GPIO.cleanup()

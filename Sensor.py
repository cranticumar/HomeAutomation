import RPi.GPIO as GPIO
from time import sleep

class Sensor(object):
    def __init__(self, name, signalGPIO, **kwargs):
        super(Sensor, self).__init__()
        self.sensor = name
        if signalGPIO is not None:
            self.signalGPIO = signalGPIO
            self.setupSignalGPIO()
        self.__dict__.update(kwargs)

    def setupSignalGPIO(self):
        GPIO.setup(self.signalGPIO, GPIO.OUT)

    def setupGPIO(self, gpio, mode):
        print 'setting GPIO {0} to {1}'.format(gpio, GPIO.IN if mode else GPIO.OUT)
        GPIO.setup(gpio, GPIO.IN if mode else GPIO.OUT)

    def setSignal(self):
        GPIO.output(self.signalGPIO, GPIO.HIGH)

    def unsetSignal(self):
        GPIO.output(self.signalGPIO, GPIO.LOW)

    def settle(self):
        sleep(2)

    def sleep(self, slp):
        sleep(slp)

    def readGPIOIN(self, gpio):
        print 'reading gpio {0}'.format(gpio)
        getinput = GPIO.input(gpio)
        return getinput
        

from Sensor import Sensor
import time

class DistanceSensor(Sensor):
    def __init__(self, trigGPIO, echoGPIO):
        super(DistanceSensor, self).__init__('Distance Sensor', trigGPIO, echoGPIO=echoGPIO)

    def measureDistance(self):
        distance = 0
        self.setupGPIO(self.echoGPIO, True)
        #GPIO.output(self.signalGPIO, False)
        self.unsetSignal()
        print "Waitng For Sensor To Settle"
        self.settle()

        #GPIO.output(TRIG, True)
        self.setSignal()
        self.sleep(0.00001)
        #GPIO.output(TRIG, False)
        self.unsetSignal()

        while self.readGPIOIN(self.echoGPIO)==0:
            pass
        pulse_start = time.time()

        while self.readGPIOIN(self.echoGPIO)==1:
            pass
        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2) - 0.5

        if distance > 2 and distance < 400:
            print "Distance: {0}cm".format(distance)
        else:
            print "Out Of Range"

        return distance

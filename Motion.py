from Sensor import Sensor
import time

class MotionSensor(Sensor):
    def __init__(self, trigGPIO):
        super(DistanceSensor, self).__init__('Motion Sensor', trigGPIO)

    def detectMotion(self):
        motionDetected = 0
        self.setupGPIO(self.echoGPIO, True)
        self.unsetSignal()
        print "Waitng For Sensor To Settle"
        self.settle()

        self.setSignal()
        self.sleep(0.00001)
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

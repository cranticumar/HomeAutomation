from Sensor import Sensor
import time

class MotionSensor(Sensor):
    def __init__(self, trigGPIO, echoGPIO):
        super(MotionSensor, self).__init__('Motion Sensor', trigGPIO, echoGPIO=echoGPIO)

    def detectMotion(self):
        self.setupGPIO(self.echoGPIO, True)

        while True:
            motion = self.readGPIOIN(self.echoGPIO)
            if motion == 0:
                print "No intruders"
                self.unsetSignal()
            elif motion == 1:
                print "Intruder(s) detected"
                self.setSignal()
            time.sleep(2)
        

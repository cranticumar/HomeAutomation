from Sensor import Sensor
import time

class SmokeSensor(Sensor):
    def __init__(self, trigGPIO, echoGPIO):
        super(SmokeSensor, self).__init__('Smoke Sensor', trigGPIO, echoGPIO=echoGPIO)

    def detectSmoke(self):
        self.setupGPIO(self.echoGPIO, True)

        while True:
            smoke = self.readGPIOIN(self.echoGPIO)
            if smoke == 0:
                print "Smoke Detected"
                self.unsetSignal()
            elif smoke == 1:
                print "No Smoke, Environment clean"
                self.setSignal()
            time.sleep(2)

from Sensor import Sensor
import time
import DHT22
import pigpio

class TempHumSensor(Sensor):
    def __init__(self, trigGPIO, echoGPIO):
        super(TempHumSensor, self).__init__('Temperature and Humidity Sensor', trigGPIO, echoGPIO=echoGPIO)

    def measureTempHum(self):
        pi = pigpio.pi()
        s = DHT22.sensor(pi, self.echoGPIO)
        s.trigger()
        time.sleep(0.03)
        print s.humidity()/1.0
        print s.temperature() / 1.0
        s.cancel()
        pi.stop()
        

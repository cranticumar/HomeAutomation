from Sensor import Sensor
import time

class TempHumSensor(Sensor):
    def __init__(self, trigGPIO, echoGPIO):
        super(TempHumSensor, self).__init__('Temperature and Humidity Sensor', trigGPIO, echoGPIO=echoGPIO)

    def measureTempHum(self):
        import DHT22
        import pigpio
        import os
        os.system('sudo pigpiod')
        pi = pigpio.pi()
        s = DHT22.sensor(pi, self.echoGPIO)
        s.trigger()
        time.sleep(0.03)
        print 'humdity is {0}'.format(s.humidity()/1.0)
        print 'temperature is {0}'.format(s.temperature() / 1.0)
        s.cancel()
        time.sleep(0.5)
        pi.stop()
        

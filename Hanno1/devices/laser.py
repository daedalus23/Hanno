from math import sqrt
import RPi.GPIO as GPIO
import time


class Laser:

    def __init__(self, servicesXML):
        self.device = servicesXML
        self.timeout = self.device.configuration["timeout"]
        self.pin = self.device.configuration["pin"]
        self.setwarning = self.device.configuration["setwarnings"]
        self.cycle = self.device.attributes["cycle"]
        self.multiplier = self.device.attributes["multiplier"]
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(self.setwarning)
        GPIO.setup(self.pin, GPIO.OUT)

    def flash(self):
        endTime = (time.time() + self.timeout)
        while endTime > time.time():
            self.on()
            time.sleep(sqrt(self.cycle*self.multiplier))
            self.off()
            time.sleep(self.cycle)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

import RPi.GPIO as GPIO


class Proximity:

    def __init__(self, servicesXML):
        self.device = servicesXML
        self.pin = self.device.configuration["pin"]
        self.setwarnings = self.device.configuration["setwarnings"]
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(self.setwarnings)
        GPIO.setup(self.pin, GPIO.IN)

    def state(self):
        if GPIO.input(self.pin) != GPIO.HIGH:
            return True
        else:
            return False

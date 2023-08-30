from .proximity import Proximity
from RpiMotorLib import RpiMotorLib
import RPi.GPIO as GPIO
import itertools
import time


class Stepper:

    def __init__(self, stepperXML, proximityXML):
        # define GPIO pins
        self.device = stepperXML
        self.proximity = Proximity(proximityXML)
        self.GPIO_pins = (
            self.device.configuration["GPIO_pin_1"],  # Micro-step Resolution MS1-MS3 -> GPIO Pin
            self.device.configuration["GPIO_pin_2"],
            self.device.configuration["GPIO_pin_3"]
        )
        self.direction = self.device.configuration["direction"]  # Direction -> GPIO Pin
        self.step = self.device.configuration["step_pin"]  # Step -> GPIO Pin
        self.motorType = self.device.configuration["motor_type"]
        # Declare a named instance of class pass GPIO pins numbers
        self.mymotortest = RpiMotorLib.A4988Nema(self.direction, self.step, self.GPIO_pins, self.motorType)

    def run(self, clockwise=True, steptype="1/8", steps=1, stepdelay=0.0004, verbose=False, initdelay=0.00001):
        self.mymotortest.motor_go(clockwise=clockwise, steptype=steptype, steps=steps, stepdelay=stepdelay,
                                  verbose=verbose, initdelay=initdelay)
        if self.proximity.state():
            return True

    def cycle(self):
        cycleDirection = True
        while True:
            if self.run(clockwise=cycleDirection):
                cycleDirection = False
                for _ in range(200):
                    self.run(clockwise=cycleDirection)
            elif self.run(clockwise=cycleDirection):
                cycleDirection = True
                for _ in range(200):
                    self.run(clockwise=cycleDirection)

    def home(self):
        leftBound = False
        rightBound = False
        home_completion = False
        while not home_completion:
            for _ in range(200):
                self.run(clockwise=False)
            while not leftBound:
                self.run(clockwise=False)
                if self.proximity.state():
                    leftBound = True
                    break
            for _ in range(200):
                self.run(clockwise=True)
            while not rightBound:
                self.run(clockwise=True)
                if self.proximity.state():
                    break
            home_completion = True
        print("Completed Homing Theta")

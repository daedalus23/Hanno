from RpiMotorLib import RpiMotorLib

import RPi.GPIO as GPIO
import time

#define GPIO pins
GPIO_pins = (18, 15, 14) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 25       # Direction -> GPIO Pin
step = 24      # Step -> GPIO Pin


# Declare a named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


def setup_gpio(pins):
    GPIO.setmode(GPIO.BCM)
    for pin in pins.values():
        GPIO.setup(pin[0], pin[1])


sleepTime = 3
 
stepDelay = 0.0004
stepType = "1/8"
travelCounts = 900
movementDir = "right"


if movementDir == "right":
    movementDir = False
elif movementDir == "left":
    movementDir = True

def run():
    while True:
        mymotortest.motor_go(movementDir, stepType, travelCounts, stepDelay, False, .05)
        # mymotortest.motor_go(movementDir, stepType, travelCounts, stepDelay, False, .05)
        # mymotortest.motor_go(movementDir, stepType, travelCounts, stepDelay, False, .05)
        # mymotortest.motor_go(movementDir, stepType, travelCounts, stepDelay, False, .05)
        # time.sleep(0.1)
        # mymotortest.motor_go(True, stepType, travelCounts, stepDelay, False, .05)
        # mymotortest.motor_go(True, stepType, travelCounts, stepDelay, False, .05)
        # mymotortest.motor_go(True, stepType, travelCounts, stepDelay, False, .05)
        # mymotortest.motor_go(True, stepType, travelCounts, stepDelay, False, .05)


# motor_go(clockwise=False, steptype="Full", steps=200, stepdelay=.005, verbose=False, initdelay=.05)

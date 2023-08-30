import RPi.GPIO as GPIO
import time as time


class Servo:
    device = None

    def __init__(self, servicesXML):
        self.device = servicesXML
        self.pin = self.device.configuration["pin"]
        self.freq = self.device.configuration["freq"]
        self.highPosition = self.device.configuration["high_position"]
        self.lowPosition = self.device.configuration["low_position"]
        self.midPosition = round((((self.lowPosition - self.highPosition) / 2) + self.highPosition), 1)
        self.moveDelay = self.device.configuration["move_delay"]
        self.setpoint = self.device.attributes["cycle_movement_setpoint"]
        self.cycleDelay = self.device.configuration["cycle_delay"]
        self.initializationPoint = self.device.configuration["initialization_point"]
        self.setwarnings = self.device.configuration["setwarnings"]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.setwarnings(self.setwarnings)

    def servo_cycle(self):
        p = GPIO.PWM(self.pin, self.freq)
        p.start(int(self.initializationPoint))   # Initialization
        try:
            while True:
                while self.setpoint <= self.highPosition:
                    if self.setpoint >= self.lowPosition:
                        p.ChangeDutyCycle(self.setpoint)
                    self.setpoint += 0.1
                    time.sleep(self.cycleDelay)
                while self.setpoint >= self.lowPosition:
                    if self.setpoint <= self.highPosition:
                        p.ChangeDutyCycle(self.setpoint)
                    self.setpoint -= 0.1
                    time.sleep(self.cycleDelay)
        except KeyboardInterrupt:
            p.stop()
            GPIO.cleanup()

    def manual_move(self, setpoint=None):
        p = GPIO.PWM(self.pin, self.freq)
        p.start(0)  # Initialization
        try:
            if setpoint is None:
                setpoint = float(input("Enter set point value: "))
            p.ChangeDutyCycle(float(self.setpoint))
            time.sleep(0.1)
        except KeyboardInterrupt:
            p.stop()
            GPIO.cleanup()

    def home(self):
        p = GPIO.PWM(self.pin, self.freq)  # PWM with 50Hz
        p.start(0)  # Initialization
        try:
            p.ChangeDutyCycle(self.lowPosition)
            time.sleep(self.moveDelay)
            p.ChangeDutyCycle(self.highPosition)
            time.sleep(self.moveDelay)
            p.ChangeDutyCycle(self.midPosition)
            time.sleep(self.moveDelay)
            p.ChangeDutyCycle(self.midPosition)
            print("Completed Homing X")
        except KeyboardInterrupt:
            p.stop()
            GPIO.cleanup()

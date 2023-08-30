#!/usr/bin/python

from configreader import Configuration
from .calculator import Calculator
from .module import Module


import time
import csv


configPath = r"Hanno1/bin/compass_config.ini"
configCache = Configuration(configPath)


class Compass:

    raw_x_out = None
    raw_y_out = None
    raw_z_out = None

    sample_scale = 10

    def __init__(self):
        self.device = Module(configCache)
        self.device_config = {
            "hmc_setting": configCache.content["hmc_setting"],
            "hmc_config": configCache.content["hmc_config"],
            "hmc_pinout": configCache.content["hmc_pinout"]
        }
        self.configer_device()

    def configer_device(self):
        """Configer I2C device with configuration settings listed in './bin/compass_config.ini'"""
        self.device.write_byte(int(self.device_config["hmc_setting"]["register_a"]),
                                int(self.device_config["hmc_config"]["register_a"], 2))  # Set to 8 samples @ 15Hz

        self.device.write_byte(int(self.device_config["hmc_setting"]["register_b"]),
                                int(self.device_config["hmc_config"]["register_b"], 2))  # 1.3 gain LSb / Gauss 1090 (default)

        self.device.write_byte(int(self.device_config["hmc_setting"]["register_c"]),
                               int(self.device_config["hmc_config"]["register_c"], 2))  # Continuous-Measurement Mode

    def collect_raw_data(self):
        """Collect raw 'X,Y,Z' data from I2C device"""
        self.raw_x_out = self.device.read_word_2c(int(self.device_config["hmc_pinout"]["x"]))
        self.raw_y_out = self.device.read_word_2c(int(self.device_config["hmc_pinout"]["y"]))
        self.raw_z_out = self.device.read_word_2c(int(self.device_config["hmc_pinout"]["z"]))

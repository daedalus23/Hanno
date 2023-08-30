from xmlreader import LoadXML

from .laser import Laser
from .proximity import Proximity
from .servo import Servo
from .stepper import Stepper


class DeviceController:

    def __init__(self, serviceConfig):
        self.deviceInstances = {
            "laser": {
                "class": Laser(LoadXML(serviceConfig, "laser")),
                "config": LoadXML(serviceConfig, "laser")
            },
            "servo": {
                "class": Servo(LoadXML(serviceConfig, "servo")),
                "config": LoadXML(serviceConfig, "servo")
            },
            "stepper": {
                "class": Stepper(
                    LoadXML(serviceConfig, "stepper"),
                    LoadXML(serviceConfig, "proximity")
                ),
                "config": LoadXML(serviceConfig, "stepper")
            }
        }

    def run_command(self, device, command):
        getattr(self.deviceInstances[device]["class"], command)()

    def is_cmd_continuous(self, inputFuncs):
        if self.deviceInstances[inputFuncs['device']]['config'].actions[inputFuncs['commandId']]['continuous']:
            return False
        else:
            return True

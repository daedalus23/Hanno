from devices import DeviceController

import threading
import time


class Scheduler:
    def __init__(self, funcs, servicesXML="/home/pi/Hanno1/bin/services.xml"):
        self.restart_flag = True
        self.threads = []
        self.funcs = funcs
        self.deviceController = DeviceController(servicesXML)

    def run_command(self):
        for command in self.funcs:
            if self.deviceController.is_cmd_continuous(command):
                t = threading.Thread(target=self.deviceController.run_command, args=[command['device'], command['commandId']])
                t.start()
                self.threads.append(t)

        for command in self.funcs:
            if not self.deviceController.is_cmd_continuous(command):
                t = threading.Thread(target=self.continuous_func, args=[command['device'], command['commandId']])
                t.start()
                self.threads.append(t)

        # Wait for all threads to complete
        for thread in self.threads:
            thread.join()
        return True

    def continuous_func(self, device, command, cycles=1):
        while self.restart_flag:
            for _ in range(cycles):
                self.deviceController.run_command(device, command)
            self.restart_flag = False

from multithreading import Scheduler

import sys


def command_parser(args):
    listCommands = [i.strip(" ").split(":") for i in args.split(";")]
    commands = []
    for item in listCommands:
        commands.append({
            "device": item[0],
            "commandId": item[1]
        })
    return commands


def main():

    bootup = "stepper:home; servo:home; laser:flash"
#    rawCommands = "laser:flash"
    threads = Scheduler(command_parser(bootup))
    threads.run_command()
#    for _ in range(1):
#        threads = Scheduler(command_parser(rawCommands))
#        threads.run_command()


if __name__ == "__main__":
    main()

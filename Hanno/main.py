from stepper.stepper import run
from proximity import Proximity
from laser import Laser


def main():
    steps = 1
    laser = Laser()
    proximity = Proximity()
    laser.on()
    tic = 0
    while proximity.state():
        run(clockwise=False, steptype="1/8", steps=tic, stepdelay=.0004, verbose=False, initdelay=.05)
        tic += 1
    laser.off()

if __name__ == "__main__":
    main()

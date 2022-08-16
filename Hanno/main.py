from stepper.stepper import run
from laser import Laser


def main():
    steps = 1
    laser = Laser()
    laser.on()
    for i in range(steps):
        run()
        print(f"On step {i} of {steps}")
    laser.off()
    print("Completed!")


if __name__ == "__main__":
    main()

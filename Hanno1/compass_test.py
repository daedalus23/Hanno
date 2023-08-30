import time

from prime_compass import Compass


def main():
    compass = Compass()
    for _ in range(10):
        compass.collect_raw_data()
        print(f"X: {compass.raw_x_out}, Y: {compass.raw_y_out}, Z: {compass.raw_z_out}")
        time.sleep(1)


if __name__ == "__main__":
    main()

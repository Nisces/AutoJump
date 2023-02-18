import cv2

from calculator.template_calculator import TemplateCalculator
from toucher.adb_toucher import ADBToucher
from watcher.adb_watcher import ADBWatcher


def main():
    watcher = ADBWatcher()
    toucher = ADBToucher()
    calculator = TemplateCalculator()

    # img = watcher.get_image()
    img = cv2.imread('screen.png')
    distance = calculator.get_distance(img)
    toucher.touch(distance)
    cv2.imshow('screen', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

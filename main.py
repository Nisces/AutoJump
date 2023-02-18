# This is a sample Python script.
import os

import cv2


def main():
    # while True:
    output = os.popen('adb shell screencap -p > screen.png')
    print(output.read())
    screen = cv2.imread('screen.png')
    cv2.imshow('screen', screen)
    cv2.waitKey(0)


def image_process():
    screen = cv2.imread('screen.png')
    cv2.imshow('screen', screen)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

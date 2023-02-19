import os

import cv2

from .watcher import Watcher


class ADBWatcher(Watcher):
    IMAGE_NAME = 'screen.png'

    def __init__(self):
        output = os.popen('adb devices')
        # print(output.read())

    def __del__(self):
        # os.popen(f'adb shell rm /sdcard/{self.IMAGE_NAME}')
        # print('delete temp screen.png image')
        pass

    def get_image(self) -> cv2.Mat:
        # adb screenshot save image to screen.png
        output = os.system(f'adb shell screencap -p > {self.IMAGE_NAME}')
        # output = os.popen(f'adb pull /sdcard/{self.IMAGE_NAME} {self.IMAGE_NAME}')
        # print(output.read())
        # os.popen(f'adb shell rm /sdcard/{self.IMAGE_NAME}')
        # opencv read image and return
        image = cv2.imread(self.IMAGE_NAME)
        return image

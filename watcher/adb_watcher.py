import os

import cv2

from .watcher import Watcher


class ADBWatcher(Watcher):
    IMAGE_NAME = 'screen.png'
    CHEESE_IMAGE = 'cheese.png'

    def __init__(self):
        output = os.popen('adb devices')
        print(output.read())

    def get_image(self) -> cv2.Mat:
        # adb screenshot save image to screen.png
        output = os.popen(f'adb shell screencap -p > {self.IMAGE_NAME}')
        print('adb screencap output = ' + output.read())
        # opencv read image and return
        image = cv2.imread(self.IMAGE_NAME)
        return image

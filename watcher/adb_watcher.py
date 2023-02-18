import os

import cv2

from .watcher import Watcher


class ADBWatcher(Watcher):
    IMAGE_NAME = 'screen.png'

    def get_image(self) -> cv2.Mat:
        output = os.popen(f'adb shell screencap -p > {self.IMAGE_NAME}')
        print(output.read())
        image = cv2.imread(self.IMAGE_NAME)
        return image

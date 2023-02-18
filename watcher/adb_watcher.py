import os

import cv2

from .watcher import Watcher


class ADBWatcher(Watcher):
    IMAGE_NAME = 'screen.png'
    CHEESE_IMAGE = 'cheese.png'

    def get_image(self) -> cv2.Mat:
        output = os.popen(f'adb shell screencap -p > {self.IMAGE_NAME}')
        print(output.read())
        image = cv2.imread(self.IMAGE_NAME)
        return image

    def get_object(self, img: cv2.Mat):
        tmpl = cv2.imread(self.CHEESE_IMAGE)
        res = cv2.matchTemplate(img, tmpl, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(min_val, max_val, min_loc, max_loc)

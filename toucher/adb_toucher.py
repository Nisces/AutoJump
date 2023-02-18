import os

from .toucher import Toucher


class ADBToucher(Toucher):
    FACTOR = 0.85

    def touch(self, distance: float):
        output = os.popen('adb devices')
        print(output.read())
        output = os.popen('adb shell input keyevent 82')
        print(output.read())

    def get_touch_time(self, distance: float):
        return distance / self.FACTOR

import os

from .toucher import Toucher


class ADBToucher(Toucher):
    FACTOR = 0.85

    def __init__(self):
        output = os.popen('adb devices')
        print(output.read())

    # 触控操作
    def touch(self, distance: float):
        # 获取点击持续时间
        time = self.get_touch_time(distance)
        # 使用adb发送点击命令
        os.popen(f'adb shell input swipe 0 0 0 0 {time}')

    def get_touch_time(self, distance: float):
        return distance * self.FACTOR

from abc import ABCMeta, abstractmethod

import cv2


class Calculator(metaclass=ABCMeta):
    @abstractmethod
    def get_distance(self, mat: cv2.Mat):
        pass

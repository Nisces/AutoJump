from abc import ABCMeta, abstractmethod

import cv2


class Calculator(metaclass=ABCMeta):
    @abstractmethod
    def get_distance(self, img: cv2.Mat) -> float:
        pass

from abc import ABCMeta, abstractmethod

import cv2


class Watcher(metaclass=ABCMeta):
    @abstractmethod
    def get_image(self) -> cv2.Mat:
        pass

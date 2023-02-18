from abc import ABCMeta, abstractmethod


class Toucher(metaclass=ABCMeta):
    @abstractmethod
    def touch(self, distance):
        pass

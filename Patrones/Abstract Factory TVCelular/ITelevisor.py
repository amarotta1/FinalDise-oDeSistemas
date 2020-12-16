from abc import ABC, abstractmethod


class Televisor(ABC):    # ProductA
    @abstractmethod
    def funcion_televisor(self):
        pass

from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def crear_cuenta(self):
        pass

    @abstractmethod
    def crear_credito(self):
        pass

    @abstractmethod
    def crear_debito(self):
        pass
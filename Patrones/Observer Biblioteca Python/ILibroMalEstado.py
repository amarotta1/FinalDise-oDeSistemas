from abc import ABC,abstractmethod

class ILibroMalEstado(ABC):
    @abstractmethod
    def update(self):
        pass



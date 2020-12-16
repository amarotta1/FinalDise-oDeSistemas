from abc import ABC,abstractmethod

class Subject(ABC):
    @abstractmethod
    def agregar(self,observer):
        pass

    @abstractmethod
    def eliminar(self,observer):
        pass

    @abstractmethod
    def notificar(self):
        pass



from abc import ABC, abstractmethod

class Persona(ABC):
    #aquellos que implementen esta interfaz deberan sobreescribir este metodo
    @abstractmethod
    def profesion(self):
        pass

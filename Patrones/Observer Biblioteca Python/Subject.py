from abc import ABC,abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self):
        pass
    
    @abstractmethod
    def dettach(self):
        pass
    
    @abstractmethod
    def notifyObservers(self):
        pass


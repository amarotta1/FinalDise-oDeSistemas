#Interface Element
from abc import ABC,abstractmethod

class Figure(ABC):
    
    @abstractmethod
    def accept(self,figure):
        pass
        


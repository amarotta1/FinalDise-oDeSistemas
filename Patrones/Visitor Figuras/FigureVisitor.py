#Interface Visitor
from abc import ABC,abstractmethod

class FigureVisitor():
    @abstractmethod
    def visitCircle(self,circle):
        pass
    
    @abstractmethod
    def visitSquare(self,square):
        pass
    
    @abstractmethod
    def visitTriangle(self,triangle):
        pass
    



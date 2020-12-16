from Figure import Figure
from math import pi
from math import inf

class Circle(Figure):

    def __init__(self,name,radius):

        self.name = name
        self.radius = radius

    def getRadius(self):
        return self.radius

    def accept(self,figureVisitor):
        figureVisitor.visitCircle(self)



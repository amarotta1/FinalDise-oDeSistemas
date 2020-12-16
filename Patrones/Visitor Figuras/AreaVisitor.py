from FigureVisitor import FigureVisitor
from math import pi

class AreaVisitor(FigureVisitor):

    def __init__(self):
        self.totalArea = 0

    def visitCircle(self,circle):
        self.totalArea = 0
        self.totalArea += pi * circle.getRadius() * circle.getRadius()
        print(circle.name+ ': '+str(self.totalArea))

    def visitSquare(self,square):
        self.totalArea = 0
        self.totalArea += square.getSide() * square.getSide()
        print(square.name+ ': '+str(self.totalArea))

    def visitTriangle(self,triangle):
        self.totalArea = 0
        self.totalArea += triangle.getBase() * triangle.getHeight() * 0.5
        print(triangle.name+ ': '+str(self.totalArea))


    def process(self,figures):
        for figure in figures:
            figure.accept(self)
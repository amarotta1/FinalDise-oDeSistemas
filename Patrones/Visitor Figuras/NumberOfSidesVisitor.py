from FigureVisitor import FigureVisitor
from math import inf

class NumeberOfSidesVisitor(FigureVisitor):

    def __init__(self):
        self.total = 0


    def visitCircle(self,circle):
        self.total = 0
        self.total += inf
        print(circle.name +': ' +str(self.total))

    def visitSquare(self,square):
        self.total = 0
        self.total += 4
        print(square.name +': ' +str(self.total))

    def visitTriangle(self,triangle):
        self.total = 0
        self.total += 3
        print(triangle.name +': ' +str(self.total))

   
    def process(self,figures):
        for figure in figures:
            figure.accept(self)
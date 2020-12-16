from AreaVisitor import AreaVisitor
from NumberOfSidesVisitor import NumeberOfSidesVisitor
from Circle import Circle
from Square import Square
from Triangle import Triangle

class Cliente():

    def __init__(self):
        self.figures = []

    def add(self,figure):
        self.figures.append(figure)

    def totalArea(self):
        areaVisitor = AreaVisitor()
        areaVisitor.process(self.figures)
        

    def totalNumberOfSides(self):
        
        nosVisitor = NumeberOfSidesVisitor()
        nosVisitor.process(self.figures)
        

if __name__ == "__main__":

    c = Circle('Circulo 1',3)
    s = Square('Cuadrado 1',5)
    t = Triangle('Triangulo 1',3,5)

    cliente = Cliente()

    cliente.add(c)
    cliente.add(s)
    cliente.add(t)
    print('\nAreas')
    cliente.totalArea()
    print('\nLados')
    cliente.totalNumberOfSides()

    c2 = Circle('Circulo 2',5)
    s2 = Square('Cuadrado 2',6)
    t2 = Triangle('Triangulo 2',2,4)

    cliente.add(c2)
    cliente.add(s2)
    cliente.add(t2)
    print('\nAreas')
    cliente.totalArea()
    print('\nLados')
    cliente.totalNumberOfSides()
    
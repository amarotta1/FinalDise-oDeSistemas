from Figure import Figure

class Triangle():
    def __init__(self,name,base,height):
        self.name = name
        self.base = base
        self.height = height


    def getBase(self):
        return self.base

    def getHeight(self):
        return self.height

    def accept(self,figureVisitor):
        figureVisitor.visitTriangle(self)



from Figure import Figure

class Square():

    def __init__(self,name,side):
        self.name = name
        self.side = side

    def getSide(self):
        return self.side

    def accept(self,figureVisitor):
        figureVisitor.visitSquare(self)

    
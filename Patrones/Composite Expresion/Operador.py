from Expresion import Expresion


class Operador(Expresion):

    def __init__(self,expresion1,expresion2):
        self.expresion1 = expresion1
        self.expresion2 = expresion2


    def getExpresion1(self):
        return self.expresion1

    def getExpresion2(self):
        return self.expresion2

    def operador(self):
        pass

    def imprimir(self):
        return "(" + self.getExpresion1().imprimir() + self.operador() + self.getExpresion2().imprimir() + ")"
        


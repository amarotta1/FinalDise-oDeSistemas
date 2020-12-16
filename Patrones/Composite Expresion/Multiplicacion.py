from Operador import Operador

class Multiplicacion(Operador):

    def __init__(self,expresion1,expresion2):
        Operador.__init__(self,expresion1,expresion2)

    def calcular(self):

        return self.getExpresion1().calcular() * self.getExpresion2().calcular()

    def operador(self):
        return "*"
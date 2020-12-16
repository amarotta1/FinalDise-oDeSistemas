from Expresion import Expresion
#Hoja
class Numero(Expresion):

    def __init__(self,numero):        
        self.numero = numero
      
    def calcular(self):
        return self.numero

    def imprimir(self):
        return str(self.numero)


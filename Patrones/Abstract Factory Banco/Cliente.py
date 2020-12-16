from FactoryBlack import FactoryBlack
from FactoryGold import FactoryGold

class Cliente():

    def __init__(self):
        self.cuenta = None
        self.credito = None
        self.debito = None

    def usar_factory(self,factory):
        self.cuenta = factory.crear_cuenta()
        self.credito = factory.crear_credito()
        self.debito = factory.crear_debito()



if __name__ == "__main__":
    
    clienteGold = Cliente()

    clienteGold.usar_factory(FactoryGold())

    print('\n Cliente usando su cuenta y tarjetas\n')

    
    clienteGold.cuenta.funcion()
    clienteGold.credito.funcion()
    clienteGold.debito.funcion()






from AbstractFactory import AbstractFactory
from CreditoGold import CreditoGold
from CuentaGold import CuentaGold
from DebitoGold import DebitoGold



class FactoryGold(AbstractFactory):

    def crear_cuenta(self):
        print('Creando una cuenta Gold')
        return CuentaGold()

    def crear_credito(self):
        print('Creando una tarjeta de credito Gold')
        return CreditoGold()

    def crear_debito(self):
        print('Creando una tarjeta de debito Gold')
        return DebitoGold()
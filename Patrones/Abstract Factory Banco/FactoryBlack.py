from AbstractFactory import AbstractFactory
from CreditoBlack import CreditoBlack
from CuentaBlack import CuentaBlack
from DebitoBlack import DebitoBlack



class FactoryBlack(AbstractFactory):

    def crear_cuenta(self):
        print('Creando una cuenta Black')
        return CuentaBlack()

    def crear_credito(self):
        print('Creando una tarjeta de credito Black')
        return CreditoBlack()

    def crear_debito(self):
        print('Creando una tarjeta de debito Black')
        return DebitoBlack()
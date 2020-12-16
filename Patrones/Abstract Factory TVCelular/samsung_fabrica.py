from IFabrica import Fabrica
from samsung_televisor import SamsungTelevisor
from samsung_celular import SamsungCelular


class SamsungFabrica(Fabrica):    # ConcreteFactory2
    def crear_televisor(self):
        return SamsungTelevisor()

    def crear_celular(self):
        return SamsungCelular()

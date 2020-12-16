from Cortador import Cortador
from Freidor import Freidor
from Hervidor import Hervidor


class Cocinar(object):
    def prepararComida(self):
        self.cortador = Cortador()
        self.cortador.cortarVegetales()

        self.hervidor = Hervidor()
        self.hervidor.hervirVegetales()

        self.freidor = Freidor()
        self.freidor.freir()
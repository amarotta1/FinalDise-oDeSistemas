from Banco import Banco

class SectorGerencia(Banco):

    def __init__(self):
        Banco.__init__(self)
        self.cantidadGerentes = 0

    def getCantidadGerentes(self):
        return self.cantidadGerentes

    def setCantidadGerentes(self,cantidadGerentes):
        self.cantidadGerentes = cantidadGerentes



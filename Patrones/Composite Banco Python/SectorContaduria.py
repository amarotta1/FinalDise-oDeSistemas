from Banco import Banco

class SectorContaduria(Banco):

    def __init__(self):
        Banco.__init__(self)
        self.cantidadContadores = 0

    def getCantidadContadores(self):
        return self.cantidadContadores

    def setCantidadContadores(self,cantidadContadores):
        self.cantidadContadores = cantidadContadores
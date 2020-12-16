from Banco import Banco

class SectorCajas(Banco):

    def __init__(self):
        Banco.__init__(self)
        self.cantidadCajeros = 0

    def getCantidadCajeros(self):
        return self.cantidadCajeros

    def setCantidadCajeros(self,cantidadCajeros):
        self.cantidadCajeros = cantidadCajeros
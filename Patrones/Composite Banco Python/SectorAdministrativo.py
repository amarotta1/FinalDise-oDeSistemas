from Banco import Banco

class SectorAdministrativo(Banco):

    def __init__(self):
        Banco.__init__(self)
        self.cantidadAdministradores = 0

    def getCantidadAdministradores(self):
        return self.cantidadAdministradores

    def setCantidadAdministradores(self,cantidadAdministradores):
        self.cantidadAdministradores = cantidadAdministradores
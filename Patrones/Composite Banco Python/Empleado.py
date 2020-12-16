from ISueldo import ISueldo

class Empleado(ISueldo):

    def __init__(self,nombre,cargo,sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def getCargo(self):
        return self.cargo
    def getNombre(self):
        return self.nombre
    def getSueldo(self):
        return self.sueldo

    def setCargo(self,cargo):
        self.cargo = cargo
    def setNombre(self,nombre):
        self.nombre = nombre
    def setSueldo(self,sueldo):
        self.sueldo = sueldo
    

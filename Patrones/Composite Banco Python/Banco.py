from ISueldo import ISueldo

class Banco(ISueldo):

    def __init__(self):
        self.empleados = []

    def agregar(self,sueldo):
        self.empleados.append(sueldo)

    def getSueldo(self):
        sumador = 0
        for empleado in self.empleados:
            sumador = sumador + empleado.getSueldo()

        return sumador



    

    

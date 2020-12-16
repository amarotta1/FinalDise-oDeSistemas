from Licenciado import Licenciado
from Ingeniero import Ingeniero
from Contador import Contador

class Factory():

    #Estatico para no necesitar una instancia de la Fabrica, por eso no se le pasa el self
    @staticmethod
    def crear(profesion):
        if profesion == 'Licenciado':            
            return Licenciado()

        if profesion == 'Contador':
            return Contador()

        if profesion == 'Ingeniero':
            return Ingeniero() 


from mujer import Mujer
from hombre import Hombre 


class Factory(object):

    def get_persona(self, nombre, genero, edad, nacionalidad):
        if genero.upper() == 'F':
            return Mujer(nombre, edad, genero, nacionalidad)
        elif genero.upper() == 'M':
            return Hombre(nombre, edad, genero, nacionalidad)

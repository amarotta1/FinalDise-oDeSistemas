from persona import Persona


class Hombre(Persona):

    def __init__(self, nombre, edad, genero, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad
        print("\nSoy hombre")
        print("Mi nombre es "+nombre+", sexo "+genero+", tengo "+edad+" años y vivo en "+nacionalidad)

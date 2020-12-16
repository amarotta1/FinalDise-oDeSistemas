class Persona(object):
	"""La persona cuenta con un nombre,
    su edad, genero y nacionalidad """
	def __init__(self):
		self.nombre = None
		self.edad = None
		self.genero = None

    
	def get_nombre(self):
		return self.nombre

	def get_edad(self):
		return self.edad

	def get_genero(self):
		return self.genero.upper()

	def get_nacionalidad(self):
		return self.nacionalidad
        
	def __str__(self):
		return "\nInformacion de una persona:\n1. Nombre: {n}\n2. Edad: {e}\n3. Genero: {g}\n4. Pais: {p}".format(
			n=self.get_nombre(), e=self.get_edad(), g=self.get_genero(), p=self.get_nacionalidad())

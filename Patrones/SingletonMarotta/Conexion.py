""" esta es una forma en la que adaptamos el modelo que usamos en java para python, pero no es la correcta
La correcta es usando decoradores """

class Conexion():

    #instancia privada
    __instance = None
  
    #es un metodo estatico, por lo tanto no se le pasa el self, se le pasa la clase con cls
    def __new__(cls):
        if Conexion.__instance is None:
            print('Creando primera y unica instancia')
            Conexion.__instance = object.__new__(cls)
        return Conexion.__instance

    #para mostrar el id de la instancia cuando imprimo    
    def conectar(self):
        print(f'Me conecto a la BD con id {id(self)}')

    def desconectar(self):
        print(f'Me desconecto de la BD con id {id(self)}')

    

if __name__ == "__main__":
    #podria parecer que creo dos instancias distintas pero no lo hago.
    conexion1 = Conexion()
    conexion2 = Conexion()

    conexion1.conectar()
    conexion2.conectar()
    conexion1.desconectar()
    conexion2.desconectar()



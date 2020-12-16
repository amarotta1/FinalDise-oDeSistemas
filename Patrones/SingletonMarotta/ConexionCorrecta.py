def singleton(cls):   
    #usamos un diccionario para poder usar el decorador en varias clases y asi 'reciclarlo' 
    instances = dict()
    def wrapper(*args, **kwargs):
        if cls not in instances:
            #si en el dict no hay una clave de este tipo de clase se crea, para poder pasarle parametros de creacion
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Conexion():

    def __init__(self,nombre):
        print('Creando la primer instancia')
        self.sesion = nombre
       

    #para mostrar el id de la instancia cuando imprimo    
    def conectar(self):
        print(f'Me conecto a la BD con id {id(self)}')

    def desconectar(self):
        print(f'Me desconecto de la BD con id {id(self)}')

    

if __name__ == "__main__":
    #podria parecer que creo dos instancias distintas pero no lo hago.
    conexion1 = Conexion('SQL')
    conexion2 = Conexion()

    print(conexion1.sesion)
    print(conexion2.sesion)

    conexion1.conectar()
    conexion2.conectar()
    conexion1.desconectar()
    conexion2.desconectar()
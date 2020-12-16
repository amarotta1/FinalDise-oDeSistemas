from sony_fabrica import SonyFabrica
from samsung_fabrica import SamsungFabrica

#por ejemplo despues puedo agregar una fabrica Philco y no tendria que modificar al cliente
class Cliente():
    def codigo_cliente(self, fabrica):
        televisor = fabrica.crear_televisor()
        celular = fabrica.crear_celular()

        print(televisor.funcion_televisor())
        print(celular.funcion_celular())


if __name__ == "__main__":
    c = Cliente()
    print("Fábrica Sony: ")
    c.codigo_cliente(SonyFabrica())
    print("\n")
    print("Fábrica Samsung: ")
    c.codigo_cliente(SamsungFabrica())

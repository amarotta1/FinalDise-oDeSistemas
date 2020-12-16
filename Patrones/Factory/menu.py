from factory import Factory

class Menu():
    pass

    def menuFactory(self):
        print("\n1. ---> Ingresar una persona")
        print("2. ---> Salir")
        return int(input("\nElija una opcion: "))

if __name__ == "__main__":
    menu = Menu()
    factoria = Factory()
    Bucle = True
    while Bucle == True:
        opcion = menu.menuFactory()
        if opcion == 1:
            nom = str(input("Ingrese el nombre: "))
            sexo = str(input("Ingrese el sexo: "))
            edad = str(input("Ingrese la edad: "))
            pais = str(input("Ingrese el pais: "))
            persona = factoria.get_persona(str(nom), str(sexo).upper(), edad, str(pais))
            print(persona)
        if opcion == 2:
            Bucle = False
 
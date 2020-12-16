from Factory import Factory

if __name__ == "__main__":
    
    licenciado = Factory.crear('Licenciado')
    ingeniero = Factory.crear('Ingeniero')
    contador = Factory.crear('Contador')

    licenciado.profesion()
    ingeniero.profesion()
    contador.profesion()
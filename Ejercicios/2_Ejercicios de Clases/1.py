class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print("Su nombre es ", self.nombre)

nombre1 = input("Ingrese su nombre: ")
Persona1 = Persona(nombre1)
Persona1.imprimir()
nombre2 = input("Ingrese el nombre de su amigo: ")
Persona2 = Persona(nombre2)
Persona2.imprimir()

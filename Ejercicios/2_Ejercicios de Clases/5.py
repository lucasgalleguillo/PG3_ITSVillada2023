class Persona:
    def __init__(self ,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



class Empleado(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    def sueldo(self, sueldo):
        self.suel = sueldo
        if self.suel >= 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
sueldo = int(input("Ingrese su sueldo: "))
empleado =Empleado(nombre, apellido)
empleado.sueldo(sueldo)

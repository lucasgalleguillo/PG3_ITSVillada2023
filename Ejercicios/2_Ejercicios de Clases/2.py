class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        if self.nota >= 6:
            print (f"El alumno {self.nombre} esta aprobado con", self.nota)
        else:
            print (f"El alumno {self.nombre} esta desaprobado con", self.nota)

nombre = (input("Ingrese nombre del alumno: "))
nota = float(input("Ingrese la nota del alumno: "))
alumno = Alumno(nombre, nota)
alumno.imprimir()
nombre1 = (input("Ingrese nombre del alumnoo: "))
nota1 = float(input("Ingrese la nota del alumno: "))
alumno1 = Alumno(nombre1, nota1)
alumno1.imprimir()

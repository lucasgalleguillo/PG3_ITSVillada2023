meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

def mes():
    while True:
        try:
            num_mes = int(input("Ingrese el número de un mes (1-12): "))
            nombre_mes = meses[num_mes-1]
            print(f"El mes número {num_mes} es {nombre_mes}")
        except IndexError:
            print("El número de mes ingresado no es válido")

if __name__== "__main__":
     mes()
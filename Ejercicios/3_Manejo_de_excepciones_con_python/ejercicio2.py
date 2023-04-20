def division():
        while True:   
            try:
                op1 = (int(input("Ingrese un numero: ")))
                op2 = (int(input("Ingrese otro numero: ")))
                print(f"El resultado es: {op1 / op2}")
            except ZeroDivisionError:
                print("No se puede dividir por cero")


if __name__== "__main__":
     division()
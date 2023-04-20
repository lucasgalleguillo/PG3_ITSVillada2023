def suma():
        while True:   
            try:
                op1 = (int(input("Ingrese un numero: ")))
                op2 = (int(input("Ingrese otro numero: ")))
                print(f"El resultado es: {op1 + op2}")
            except ValueError:
                print("El valor es incorrecto")
            var = input("Quiere seguir ingresando valores?yes/no: ")
            if var == "yes":
                pass
            elif var == "no":
                 break


if __name__== "__main__":
     suma()
                
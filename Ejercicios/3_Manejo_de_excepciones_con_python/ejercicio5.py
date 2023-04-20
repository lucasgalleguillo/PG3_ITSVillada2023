def escribir(num):
        try:
            with open('archivo.txt', 'w') as archivo:
                archivo.write(num)  
        except TypeError:
            print("No se puede escribir un entero en el archivo de texto.")

if __name__== "__main__":
     escribir(1)
def es_palindromo(palabra):
    return palabra == palabra[::-1]

var = input("Ingrese una palabra: ")
print(es_palindromo(var))

def buscar_elemento(lista, elemento):
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1

lista = [8,12,9,45]
elemento = int(input("Ingrese un número: "))

indice = buscar_elemento(lista, elemento)
if indice != -1:
    print(f"El elemento {elemento} se encuentra en el índice {indice} de la lista.")
else:
    print(f"El elemento {elemento} no se encuentra en la lista.")
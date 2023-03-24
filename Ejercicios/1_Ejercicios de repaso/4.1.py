def ordenar_lista(lista):
    return sorted(lista, reverse=True)

lista = []  
while val != "a":
    val = input("Ingrese un valor para agregar a la lista o 'fin' para terminar: ")
    if val == 'a':
        break  
    lista.append(int(val))  

print( lista)
lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)
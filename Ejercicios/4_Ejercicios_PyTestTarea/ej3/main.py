def is_anagram(word1, word2):
    # Convertir las palabras a minúsculas y eliminar los espacios en blanco
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    
    # Verificar si las palabras tienen la misma longitud
    if len(word1) != len(word2):
        return False
    
    # Crear diccionarios de recuento de letras para ambas palabras
    letters_count1 = {}
    letters_count2 = {}
    
    # Contar las letras en la primera palabra
    for letter in word1:
        letters_count1[letter] = letters_count1.get(letter, 0) + 1
    
    # Contar las letras en la segunda palabra
    for letter in word2:
        letters_count2[letter] = letters_count2.get(letter, 0) + 1
    
    # Verificar si los diccionarios de recuento de letras son iguales
    if letters_count1 == letters_count2:
        return True
    else:
        return False

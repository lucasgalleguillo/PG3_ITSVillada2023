import re

def validate_password(password):
    # Verificar la longitud mínima de 8 caracteres
    if len(password) < 8:
        return False
    
    # Verificar al menos una letra mayúscula, una letra minúscula y un número
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password):
        return False
    
    # Verificar si hay caracteres especiales (no alfanuméricos)
    if re.search(r"\W", password):
        return False
    
    # Si pasa todas las verificaciones, la contraseña es válida
    return True

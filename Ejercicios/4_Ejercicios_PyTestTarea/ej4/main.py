import math

def calculate_statistics(numbers):
    # Calcula la media
    mean = sum(numbers) / len(numbers)

    # Calcula la suma de los cuadrados de las diferencias con la media
    sum_of_squared_diff = sum((x - mean) ** 2 for x in numbers)

    # Calcula la desviación estándar
    standard_deviation = math.sqrt(sum_of_squared_diff / len(numbers))

    return mean, standard_deviation

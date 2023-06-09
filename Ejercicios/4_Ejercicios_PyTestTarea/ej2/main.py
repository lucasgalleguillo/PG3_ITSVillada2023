def roman_to_decimal(roman_number):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    decimal_number = 0
    
    for i in range(len(roman_number)):
        if i > 0 and roman_map[roman_number[i]] > roman_map[roman_number[i-1]]:
            decimal_number += roman_map[roman_number[i]] - 2 * roman_map[roman_number[i-1]]
        else:
            decimal_number += roman_map[roman_number[i]]
    
    return decimal_number

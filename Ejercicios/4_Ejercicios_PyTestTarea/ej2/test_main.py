from main import roman_to_decimal

def test_roman_to_decimal():
    assert roman_to_decimal("III") == 3
    assert roman_to_decimal("IX") == 9
    assert roman_to_decimal("LVIII") == 58
    assert roman_to_decimal("MCMXCIV") == 1994

from main import is_anagram

def test_is_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False
    assert is_anagram("Debit card", "Bad credit") == True
    assert is_anagram("apple", "papel") == True

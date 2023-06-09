from main import validate_password

def test_validate_password():
    assert validate_password("Abc12345") == True
    assert validate_password("password") == False
    assert validate_password("Abc@1234") == False
    assert validate_password("") == False
    assert validate_password("Abcdefg1") == True
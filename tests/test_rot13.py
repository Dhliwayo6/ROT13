from rot13 import encrypt


def test_encrypt():
    assert encrypt("python") == "clguba"
    assert encrypt("secret") == "frperg"
    assert encrypt("password") == "cnffjbeq"

def test_encrypt_case():
    assert encrypt("Python") == "Clguba"
    assert encrypt("SeCret") == "FrPerg"
    assert encrypt("Password") == "Cnffjbeq"
    assert encrypt("ENCRYPT") == "RAPELCG"

def test_encrypt_not_in_alpha():
    assert encrypt("rot13") == "ebg13"
    assert encrypt("Pa$$w0rd") == "Cn$$j0eq"
    assert encrypt("<>@#$%^!&*()") == "<>@#$%^!&*()"


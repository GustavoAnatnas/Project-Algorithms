from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("message", "")
        encrypt_message(1, 2)
        encrypt_message("true", "true")
    assert encrypt_message("testes", -1) == "setset"
    assert encrypt_message("testes", 3) == "set_set"
    assert encrypt_message("testes", 4) == "se_tset"
    

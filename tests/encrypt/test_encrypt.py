import pytest
from challenges.challenge_encrypt_message import encrypt_message


# task 2
def test_encrypt_message():
    correct_mock = {
        "1": ["mensagem", 3],
        "2": ["mensagem", 2],
        "3": ["mensagem", -1]
    }

    error_mock = [
        {"input": ["mensagem", "3"], "output": "tipo inválido para key"},
        {"input": [123456, 3], "output": "tipo inválido para message"},
    ]

    with pytest.raises(TypeError, match=error_mock[0]["output"]):
        encrypt_message("mensagem", "3")

    with pytest.raises(TypeError, match=error_mock[1]["output"]):
        encrypt_message(123456, 3)

    assert encrypt_message(
        correct_mock["1"][0], correct_mock["1"][1]
    ) == "nem_megas"

    assert encrypt_message(
        correct_mock["2"][0], correct_mock["2"][1]
    ) == "megasn_em"

    assert encrypt_message(
        correct_mock["3"][0], correct_mock["3"][1]
    ) == "megasnem"

import pytest
from phonebook import Phonebook


@pytest.fixture(name="phonebook")
def make_phonebook():
    return_value = Phonebook()
    return_value.add("Bob", "1234")
    return_value.add("Alice", "5678")
    return return_value


def test_poc(phonebook: Phonebook):
    assert phonebook.lookup("Bob") =="1234"
    assert phonebook.lookup("Alice") =="5678"

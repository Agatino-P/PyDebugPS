import pytest
from phonebook import Phonebook


@pytest.fixture(name="phonebook")
def make_phonebook():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    phonebook.add("Alice", "5678")
    return phonebook


def test_poc(phonebook: Phonebook):
    assert phonebook.lookup("Bob") =="1234"
    assert phonebook.lookup("Alice") =="5678"

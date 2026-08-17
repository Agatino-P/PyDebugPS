import pytest
from phonebook import Phonebook


@pytest.fixture(name="phonebook")
def make_phonebook():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    return phonebook


def test_poc(phonebook):
    expected = "1234"
    result = phonebook.lookup("Bob")
    assert result == expected

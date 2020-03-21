import pytest
from validator import LengthValidator
from counter import Counter, InvalidLengthException

def test_count_repeated_valid_length():
    validator = LengthValidator(5)
    counter = Counter(validator)
    given = "aabbc"
    result = counter.count_repeated(given)
    expected = "(2)a(2)b(1)c"
    assert result == expected

def test_count_repeated_invalid_length():
    validator = LengthValidator(5)
    counter = Counter(validator)
    given = "aabbcc"
    with pytest.raises(InvalidLengthException):
        counter.count_repeated(given)
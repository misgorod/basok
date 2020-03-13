from counter import count_repeated, InvalidLengthException
import pytest

def test_count_repeated_greatedThanThirty():
    given = "1234567890123456789012345678901"
    with pytest.raises(InvalidLengthException):
        count_repeated(given)

def test_count_repeated_singleChar():
    given = "a"
    expected = "(1)a"
    actual = count_repeated(given)
    assert expected == actual

def test_count_repreated_emptyMiddle():
    given = "aaa bbc d"
    expected = "(3)a(1) (2)b(1)c(1) (1)d"
    actual = count_repeated(given)
    assert expected == actual

def test_count_repeated_multipleChars():
    given = "aabbbcdd"
    expected = "(2)a(3)b(1)c(2)d"
    actual = count_repeated(given)
    assert expected == actual

def test_count_repeated_emptyString():
    given = ""
    expected = ""
    actual = count_repeated(given)
    assert expected == actual

    
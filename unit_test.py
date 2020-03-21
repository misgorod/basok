from counter import Counter, InvalidLengthException
import pytest

class MockValidator:
    def __init__(self, answer):
        self.answer = answer

    def validate(self, text):
        return self.answer

@pytest.fixture()
def counter():
    return Counter(MockValidator(True))

def test_count_repeated_greatedThanThirty():
    counter = Counter(MockValidator(False))
    given = "1234567890123456789012345678901"
    with pytest.raises(InvalidLengthException):
        counter.count_repeated(given)

def test_count_repeated_singleChar(counter):
    given = "a"
    expected = "(1)a"
    actual = counter.count_repeated(given)
    assert expected == actual

def test_count_repreated_emptyMiddle(counter):
    given = "aaa bbc d"
    expected = "(3)a(1) (2)b(1)c(1) (1)d"
    actual = counter.count_repeated(given)
    assert expected == actual

def test_count_repeated_multipleChars(counter):
    given = "aabbbcdd"
    expected = "(2)a(3)b(1)c(2)d"
    actual = counter.count_repeated(given)
    assert expected == actual

def test_count_repeated_emptyString(counter):
    given = ""
    expected = ""
    actual = counter.count_repeated(given)
    assert expected == actual

    
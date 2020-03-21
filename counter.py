class CounterException(Exception):
    pass

class InvalidLengthException(CounterException):
    pass

class Counter:
    def __init__(self, validator):
        self.validator = validator

    def count_repeated(self, text):
        if not self.validator.validate(text): 
            raise InvalidLengthException
        if len(text) == 0:
            return ""
        prev = text[0]
        count = 0
        result = ''
        for c in text:
            if prev == c:
                count += 1
            else:
                result += f"({count}){prev}"
                count = 1
            prev = c
        result += f"({count}){prev}"
        return result 
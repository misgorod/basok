class CounterException(Exception):
    pass

class InvalidLengthException(CounterException):
    pass

def count_repeated(text):
    if len(text) > 30: 
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
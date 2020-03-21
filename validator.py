class LengthValidator:
    def __init__(self, length):
        self.length = length

    def validate(self, text):
        if len(text) > self.length:
            return False
        return True
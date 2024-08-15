import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass

def validate(value):
    return re.fullmatch(r'\d{10}', value) is not None
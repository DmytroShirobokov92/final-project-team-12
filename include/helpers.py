import re


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


def validate(value: str) -> re.Match | None:
    return re.fullmatch(r'\d{10}', value) is not None

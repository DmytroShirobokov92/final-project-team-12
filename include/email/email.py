import re
from ..helpers import Field


class Email(Field):
    def __init__(self, value: str):
        if not self.validate(value):
            raise ValueError("Invalid email format.")
        super().__init__(value)

    def validate(self, value) -> bool:
        return re.fullmatch(r'[^@]+@[^@]+\.[^@]+', value) is not None

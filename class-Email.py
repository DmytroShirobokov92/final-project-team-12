import re
from bot import Field

class Email(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid email format.")
        super().__init__(value)

    def validate(self, value):
        # Basic email validation using regex  
        return re.fullmatch(r'[^@]+@[^@]+\.[^@]+', value) is not None
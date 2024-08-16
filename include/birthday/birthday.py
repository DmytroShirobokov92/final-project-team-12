from datetime import datetime
from ..helpers import Field


class Birthday(Field):
    def __init__(self, value: str):
        super().__init__(value)
        try:
            self.value = self.validate(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def validate(self, value) -> datetime | ValueError:
        try:
            return datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")

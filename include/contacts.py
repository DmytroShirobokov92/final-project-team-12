from .birthday.birthday import Birthday
from .address.address import Address
from .email.email import Email
from .helpers import (
    Field,
    Name,
    validate
)


class Phone(Field):
    def __init__(self, value: str):
        if not validate(value):
            raise ValueError("Phone number must be 10 digits long.")
        super().__init__(value)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday = None
        self.address: Address = None
        self.emails: list[Email] = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        phone_obj = Phone(phone)  # Validate phone before removal
        self.phones = [p for p in self.phones if p.value != phone_obj.value]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone: str) -> str | None:
        phone_obj = Phone(phone)
        for p in self.phones:
            if p.value == phone_obj.value:
                return p.value
        return None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_address(self, city: str, street: str, house_number: int, apartment: int = None):
        self.address = Address(city, street, house_number, apartment)

    def add_email(self, email: str) -> None:
        self.emails.append(Email(email))

    def remove_email(self, email: str) -> None:
        email_obj = Email(email)
        self.emails = [e for e in self.emails if e.value != email_obj.value]

    def __str__(self) -> str:
        phone_str = '; '.join(p.value for p in self.phones)
        email_str = '; '.join(e.value for e in self.emails)
        birthday_str = self.birthday if self.birthday else "N/A"
        address_str = self.address if self.address else "N/A"

        table_format = (
            f"{'Contact Name':<20} | {self.name.value}\n"
            f"{'Phones':<20} | {phone_str}\n"
            f"{'Emails':<20} | {email_str}\n"
            f"{'Birthday':<20} | {birthday_str}\n"
            f"{'Address':<20} | {address_str}"
        )

        return table_format

from include.birthday.birthday import Birthday
from include.address.address import Address
from contacts_methods import validate
from helpers import (
    Field,
    Name
)

class Phone(Field):
    def __init__(self, value):
        if not validate(value):
            raise ValueError("Phone number must be 10 digits long.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = Phone(phone)  # Validate phone before removal
        self.phones = [p for p in self.phones if p.value != phone_obj.value]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        phone_obj = Phone(phone)
        for p in self.phones:
            if p.value == phone_obj.value:
                return p.value
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_address(self, city, street, house_number, apartment=None):
        self.address = Address(city, street, house_number, apartment)

    def __str__(self):
        phone_str = '; '.join(p.value for p in self.phones)
        address_str = f", address: {self.address}" if self.address else ""
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phone_str}{birthday_str}{address_str}"


import re


class Address:
    def __init__(self, city: str, street: str, house_number: int, apartment: int = None):
        self.city = validate_city(city)
        self.street = validate_street(street)
        self.house_number = validate_house_number(house_number)
        self.apartment = validate_apartment(apartment)

    def __str__(self):
        if self.apartment:
            return f"{self.city}, {self.street}, {self.house_number}, кв. {self.apartment}"
        return f"{self.city}, {self.street}, {self.house_number}"


def validate_city(city: str):
    if not re.match(r'^[A-Za-zА-Яа-я\s]+$', city):
        raise ValueError("City must contain only letters and spaces.")
    if not city.strip():
        raise ValueError("City cannot be empty.")
    return city


def validate_street(street: str):
    if not re.match(r'^[A-Za-zА-Яа-я\s]+$', street):
        raise ValueError("Street must contain only letters and spaces.")
    if not street.strip():
        raise ValueError("Street cannot be empty.")
    return street


def validate_house_number(house_number: int):
    if not re.match(r'^\d+$', house_number):
        raise ValueError("House number must be a positive integer.")
    return house_number


def validate_apartment(apartment: int):
    if apartment and not re.match(r'^\d+$', apartment):
        raise ValueError("Apartment number must be a positive integer.")
    return apartment

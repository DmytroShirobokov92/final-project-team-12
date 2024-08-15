
from .address_book.address_book import AddressBook
from .contacts import Record


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Insufficient arguments provided."
        except Exception as e:
            return str(e)

    return wrapper


@input_error
def add_contact(name, phone, book: AddressBook):
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def delete_contact(name, book: AddressBook):
    if book.find(name):
        book.delete(name)
        return "Contact deleted."
    return "Contact not found."


@input_error
def change_phone(name, old_phone, new_phone, book: AddressBook):
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    return "Contact not found."


@input_error
def show_phone(name, book: AddressBook):
    record = book.find(name)
    if record:
        phones = ', '.join(p.value for p in record.phones)
        return f"Phones for {name}: {phones}"
    return "Contact not found."


@input_error
def show_all_contacts(book: AddressBook):
    if book.data:
        return '\n'.join(str(record) for record in book.data.values())
    return "Address book is empty."


@input_error
def add_birthday(name, birthday, book: AddressBook):
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    return "Contact not found."


@input_error
def add_address(args, book: AddressBook):
    name, city, street, house_number, *apartment = args
    apartment = apartment[0] if apartment else None
    record = book.find(name)
    if record:
        record.add_address(city, street, house_number, apartment)
        return "Address added."
    return "Contact not found."


@input_error
def show_birthday(name, book: AddressBook):
    record = book.find(name)
    if record:
        if record.birthday:
            return f"Birthday for {name}: {record.birthday}"
        return "Birthday not set."
    return "Contact not found."


@input_error
def birthdays(args, book: AddressBook):
    return book.upcoming_birthdays()


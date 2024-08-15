import pickle
from contacts import (
    AddressBook,
    add_contact,
    change_phone,
    show_phone,
    show_all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
    delete_contact
)
from notes import NoteBook, add_note


def save_notes(notes, filename="notes.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(notes, f)


def load_notes(filename="notes.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NoteBook()


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def parse_input(user_input):
    return user_input.strip().split()


def main():
    book = load_data()
    notes_book = load_notes()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            save_notes(notes_book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(*args, book))

        elif command == "change":
            print(change_phone(*args, book))

        elif command == "phone":
            print(show_phone(*args, book))

        elif command == "all":
            print(show_all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(*args, book))

        elif command == "show-birthday":
            print(show_birthday(*args, book))

        elif command == "birthdays":
            print(birthdays(book))

        elif command == "delete":
            print(delete_contact(*args, book))

        elif command == "add-note" or command == "modify-note":
            print(add_note(*args, notes_book))

        elif command == "all-notes":
            print(notes_book.show_all_notes())

        elif command == "search-note":
            print(notes_book.search_notes())

        elif command == "remove-note":
            print(notes_book.delete())

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

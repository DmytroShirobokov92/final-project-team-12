from include.contacts_methods import (add_contact, change_phone, show_phone, show_all_contacts, add_birthday, add_email,
                                      show_address, show_email, show_name, show_any_matches, show_birthday, birthdays, delete_contact, add_address)

from include.notes.notes import (
    add_note, load_data, load_notes, save_data, save_notes)


def parse_input(user_input: str) -> list[str]:
    return user_input.strip().split()


def main() -> None:
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

        elif command in ["contacts-list", "all"]:
            # contacts-list
            print(show_all_contacts(book=book))

        elif command == "delete-contact":
            # delete-contact {contact_name}
            print(delete_contact(*args, book=book))

        elif command == "add-contact":
            # add-contact {contact_name} {contact_phone}
            print(add_contact(*args, book=book))

        elif command == "add-address":
            # add-address {contact_name} {city} {street} {state} {zip_code}
            print(add_address(args, book=book))

        elif command == "add-birthday":
            # add-birthday {contact_name} {contact_birthday format dd.mm.yy}
            print(add_birthday(*args, book=book))

        elif command == "change-phone":
            # change-phone {contact_name} {current_contact_phone} {new_contact_phone}
            print(change_phone(*args, book=book))

        elif command in ["show-phone", "find-phone"]:
            # show-phone {contact_phone}
            print(show_phone(*args, book=book))

        elif command in ["show-address", "find-address"]:
            # show-phone {contact_address}
            print(show_address(*args, book=book))

        elif command in ["show-email", "find-email"]:
            # show-phone {contact_email}
            print(show_email(*args, book=book))

        elif command in ["show-name", "find-name"]:
            # show-phone {contact_name}
            print(show_name(*args, book=book))

        elif command in ["show", "find"]:
            # show-phone {contact_any_value}
            print(show_any_matches(*args, book=book))

        elif command == "show-birthday":
            # show-birthday {contact_name}
            print(show_birthday(*args, book=book))

        elif command == "all-notes":
            # all-notes
            print(notes_book.show_all_notes())

        elif command == "add-note" or command == "modify-note":
            # add-note | modify-note
            print(add_note(*args, notes_book))

        elif command == "search-note":
            # search-note
            print(notes_book.search_notes())

        elif command == "remove-note":
            # remove-note
            print(notes_book.delete())

        elif command == "upcoming-birthdays":
            # upcoming-birthdays
            print(birthdays(book=book))

        elif command == "add-email":
            print(add_email(args, book=book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

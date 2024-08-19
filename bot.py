from include.contacts_methods import (add_contact, change_phone, show_phone, show_all_contacts, add_birthday, add_email,
                                      show_address, show_email, show_name, show_any_matches, show_birthday, birthdays, delete_contact, add_address)

from include.notes.notes import (
    add_note)

from include.database.database import (
    load_data, load_notes, save_data, save_notes)

from include.color_console.color_console import print_valid, print_error, colored_input


# split user's input to a list of values
def parse_input(user_input: str) -> list[str]:
    return user_input.strip().split()


def main() -> None:
    # load exits or create new data
    book = load_data()
    notes_book = load_notes()

    print_valid("Welcome to the assistant bot!")

    # loop the boot
    while True:
        user_input = colored_input("Enter a command: ")
        command, *args = parse_input(user_input)
        command = command.lower()

        if command in ["close", "exit"]:
            save_data(book)
            save_notes(notes_book)
            print_valid("Good bye!")
            break

        elif command == "hello":
            print_valid("How can I help you?")

        elif command in ["contacts-list", "all"]:
            # contacts-list
            print_valid(show_all_contacts(book=book))

        elif command == "delete-contact":
            # delete-contact {contact_name}
            print_valid(delete_contact(*args, book=book))

        elif command == "add-contact":
            # add-contact {contact_name} {contact_phone}
            print_valid(add_contact(*args, book=book))

        elif command == "add-address":
            # add-address {contact_name} {city} {street} {state} {zip_code}
            print_valid(add_address(args, book=book))

        elif command == "add-birthday":
            # add-birthday {contact_name} {contact_birthday format dd.mm.yy}
            print_valid(add_birthday(*args, book=book))

        elif command == "change-phone":
            # change-phone {contact_name} {current_contact_phone} {new_contact_phone}
            print_valid(change_phone(*args, book=book))

        elif command in ["show-phone", "find-phone"]:
            # show-phone {contact_phone}
            print_valid(show_phone(*args, book=book))

        elif command in ["show-address", "find-address"]:
            # show-phone {contact_address}
            print_valid(show_address(*args, book=book))

        elif command in ["show-email", "find-email"]:
            # show-phone {contact_email}
            print_valid(show_email(*args, book=book))

        elif command in ["show-name", "find-name"]:
            # show-phone {contact_name}
            print_valid(show_name(*args, book=book))

        elif command in ["show", "find"]:
            # show-phone {contact_any_value}
            print_valid(show_any_matches(*args, book=book))

        elif command == "show-birthday":
            # show-birthday {contact_name}
            print_valid(show_birthday(*args, book=book))

        elif command == "all-notes":
            # all-notes
            print_valid(notes_book.show_all_notes())

        elif command == "add-note" or command == "modify-note":
            # add-note | modify-note
            print_valid(add_note(*args, notes_book))

        elif command == "search-note":
            # search-note
            print_valid(notes_book.search_notes())

        elif command == "remove-note":
            # remove-note
            print_valid(notes_book.delete())

        elif command == "upcoming-birthdays":
            # upcoming-birthdays
            print_valid(birthdays(book=book))

        elif command == "add-email":
            print_valid(add_email(args, book=book))

        else:
            print_error("Invalid command.")


if __name__ == "__main__":
    main()

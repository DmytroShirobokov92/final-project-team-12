from bot import Record, AddressBook

@input_error  
def add_contact(args, book: AddressBook):
    name, phone, *other_args = args  
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    # Add phone number if provided  
    if phone:
        record.add_phone(phone)

    # Handle additional arguments for address and email  
    if len(other_args) >= 4:  # Expecting at least street, city, state, zip_code  
        street, city, state, zip_code = other_args[:4]
        record.add_address(street, city, state, zip_code)

    # Add email if provided  
    if len(other_args) > 4:
        for email in other_args[4:]:  # All remaining args are treated as emails  
            record.add_email(email)

    return message
from collections import UserDict
from ..upcoming_birthdays.upcoming_birthdays import get_upcoming_birthdays
from ..contacts import Record


class AddressBook(UserDict[str, Record]):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    # find by name and full match
    def find(self, name: str) -> Record:
        return self.data.get(name)

    # find by name and parctially match
    def find_by_name(self, name: str) -> list[Record]:
        result: list[Record] = filter(lambda rec: rec.name.value.upper(
        ).find(name.upper()) != -1, self.data.values())
        return [record for record in result]

    def find_by_email(self, email: str) -> list[Record]:
        result: list[Record] = filter(lambda rec: rec.email.value.upper(
        ).find(email.upper()) != -1, self.data.values())
        return [record for record in result]

    # find by phone and parctially match
    def find_by_phone(self, phone_to_find: int) -> list[Record]:
        phone_to_find = str(phone_to_find)

        result: list[Record] = []
        for record in self.data.values():
            for phone in record.phones:
                if str(phone).find(phone_to_find) != -1:
                    result.append(record)
                    break

        return result

    # find by address's attrubutes and parctially match
    def find_by_address(self, address: str) -> list[Record | None]:
        result: list[Record] = []

        for record in self.data.values():
            if not record.address:
                continue
            address_attributes = vars(record.address).values()
            if any(attribute.upper().find(address.upper()) != -1 for attribute in address_attributes):
                result.append(record)

        return [record for record in result]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def upcoming_birthdays(self):
        return get_upcoming_birthdays(self)

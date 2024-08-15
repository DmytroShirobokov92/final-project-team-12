from collections import UserDict
from ..upcoming_birthdays.upcoming_birthdays import get_upcoming_birthdays
from ..contacts import Record


class AddressBook(UserDict[str, Record]):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def find_by_name(self, name: str) -> list[Record]:
        result = filter(lambda rec: rec.name.value.upper(
        ).startswith(name.upper()), self.data.values())
        return [record for record in result]

    def find_by_address(self, address: str) -> list[Record | None]:
        result = []
        for record in self.data.values():
            if not record.address:
                continue
            address_attributes = vars(record.address).values()
            if any(attribute.upper().startswith(address.upper()) for attribute in address_attributes):
                result.append(record)

        return [record for record in result]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def upcoming_birthdays(self):
        return get_upcoming_birthdays(self)

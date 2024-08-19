from __future__ import annotations
from datetime import datetime, timedelta
from ..color_console.color_console import colored_input
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..address_book.address_book import AddressBook


def get_upcoming_birthdays(address_book: AddressBook) -> str:
    today = datetime.today().date()

    days_ahead = int(colored_input("Input number of days ahead: "))
    end_date = today + timedelta(days=days_ahead)

    upcoming_birthdays: dict[str, str] = {}

    for user in address_book.data.values():
        if user.birthday:
            birthday = user.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if today <= birthday_this_year <= end_date:
                formatted_date = birthday_this_year.strftime("%d.%m")
                if formatted_date in upcoming_birthdays:
                    upcoming_birthdays[formatted_date] += ", " + \
                        user.name.value
                else:
                    upcoming_birthdays[formatted_date] = user.name.value

    if not upcoming_birthdays:
        return "There are no birthdays in the selected period."

    result: list[str] = []
    for date, names in upcoming_birthdays.items():
        result.append(f"{date}: {names}")
    return "\n".join(result)

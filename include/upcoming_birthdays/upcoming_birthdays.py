from datetime import datetime, timedelta


def get_upcoming_birthdays(address_book):
    today = datetime.today().date()

    days_ahead = int(input("Input number of days ahead: "))
    end_date = today + timedelta(days=days_ahead)

    upcoming_birthdays = {}

    for user in address_book.data.values():
        if user.birthday:
            birthday = user.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if today <= birthday_this_year <= end_date:
                formatted_date = birthday_this_year.strftime("%d.%m")
                if formatted_date in upcoming_birthdays:
                    upcoming_birthdays[formatted_date] += ", " + user.name.value
                else:
                    upcoming_birthdays[formatted_date] = user.name.value

    if not upcoming_birthdays:
        return "There are no birthdays in the selected period."

    result = []
    for date, names in upcoming_birthdays.items():
        result.append(f"{date}: {names}")
    return "\n".join(result)

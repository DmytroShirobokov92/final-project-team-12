from __future__ import annotations
from collections import UserDict
from include.address_book.address_book import AddressBook
from include.contacts_methods import input_error
from ..color_console.color_console import colored_input


# class to store and edit records
class NoteBook(UserDict[str, "NoteRecord"]):
    def add_record(self, note_record: NoteRecord):
        self.data[note_record.title] = note_record

    def find(self, title: str) -> NoteRecord:
        return self.data.get(title)

    def delete(self) -> str:
        title = colored_input(
            "Enter the title of the note to delete: ").strip()
        if title in self.data:
            del self.data[title]
            return f"Note titled '{title}' has been deleted."
        return f"Note titled '{title}' not found."

    def show_all_notes(self) -> str:
        if not self.data:
            return "No notes available."

        all_notes = ""
        for note_record in self.data.values():
            all_notes += str(note_record) + "\n"
        return all_notes

    def search_notes(self) -> str:
        query = colored_input(
            "Enter a keyword or sentence to search for a note: ").strip().lower()

        found_notes = [
            str(note_record) for note_record in self.data.values()
            if query in note_record.title.lower() or query in note_record.body.lower()
        ]

        if not found_notes:
            return "No matching notes found."

        return "\n".join(found_notes)


# class to store and edit notes
class NoteRecord:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body

    def update_title(self, title: str) -> None:
        self.title = title

    def update_body(self, body: str) -> None:
        self.body = body

    def __str__(self) -> str:
        return f"Title: {self.title} \nNote Body: {self.body} \n"


@input_error
def add_note(note_book: NoteBook) -> str:
    title = colored_input("Enter the note title: ")
    body = colored_input("Enter the note body: ")

    record = note_book.find(title)
    message = "Note updated."
    if record is None:
        note_record = NoteRecord(title, body)
        note_book.add_record(note_record)
        message = "Note added."
    else:
        record.update_title(title)
        record.update_body(body)

    return message

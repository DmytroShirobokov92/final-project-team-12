from collections import UserDict
from datetime import time

from contacts import input_error


class NoteBook(UserDict):
    def add_record(self, note_record):
        self.data[note_record.title] = note_record

    def find(self, title):
        return self.data.get(title)

    def delete(self):
        title = input("Enter the title of the note to delete: ").strip()
        if title in self.data:
            del self.data[title]
            return f"Note titled '{title}' has been deleted."
        return f"Note titled '{title}' not found."

    def show_all_notes(self):
        if not self.data:
            return "No notes available."

        all_notes = ""
        for note_record in self.data.values():
            all_notes += str(note_record) + "\n"
        return all_notes

    def search_notes(self):
        query = input("Enter a keyword or sentence to search for a note: ").strip().lower()

        found_notes = [
            str(note_record) for note_record in self.data.values()
            if query in note_record.title.lower() or query in note_record.body.lower()
        ]

        if not found_notes:
            return "No matching notes found."

        return "\n".join(found_notes)


class NoteRecord:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def update_title(self, title):
        self.title = title

    def update_body(self, body):
        self.body = body

    def __str__(self):
        return f"Title: {self.title} \nNote Body: {self.body} \n"


@input_error
def add_note(note_book: NoteBook):
    title = input("Enter the note title: ")
    body = input("Enter the note body: ")

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


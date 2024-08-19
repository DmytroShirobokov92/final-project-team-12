from __future__ import annotations
import pickle
from typing import TYPE_CHECKING


from ..notes.notes import NoteBook
from ..address_book.address_book import AddressBook


def save_notes(notes, filename="notes.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(notes, f)


def load_notes(filename="notes.pkl") -> NoteBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NoteBook()


def save_data(book, filename="addressbook.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl") -> AddressBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

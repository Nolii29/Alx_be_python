#!/usr/bin/python3
"""
Main script to run the library system.
"""

from book import Book, PrintBook, EBook
from library import Library

def main():
    library = Library()

    book1 = Book("The Alchemist", "Paulo Coelho", 1988)
    book2 = PrintBook("1984", "George Orwell", 1949, 328)
    book3 = EBook("Digital Fortress", "Dan Brown", 1998, 2.5)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.list_books()

if __name__ == "__main__":
    main()

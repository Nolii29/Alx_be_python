#!/usr/bin/python3
"""
Defines Book, PrintBook, and EBook classes.
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f"{self.title} by {self.author} ({self.year})"


class PrintBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def display(self):
        return f"{super().display()} - {self.pages} pages"


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def display(self):
        return f"{super().display()} - {self.file_size}MB"


class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

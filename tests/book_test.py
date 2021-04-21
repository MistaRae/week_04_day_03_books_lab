import unittest

from models.book import Book 

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("Code")
        
    def test_book_has_name(self):
        self.assertEqual("Code", self.book.title)
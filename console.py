import pdb

from models.book import Book 
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Frank Herbert")
author_repository.save(author_1)
author_2 = Author("George R.R. Martin")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("Dune")
book_repository.save(book_1)
book_2 = Book("GoT")
book_repository.save(book_2)

pdb.set_trace()
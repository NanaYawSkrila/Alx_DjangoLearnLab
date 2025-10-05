from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books_by_author = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:", books_by_author)

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for Central Library:", librarian)

from relationship_app.models import Author, Book, Library, Librarian
from django.contrib.auth.models import User

# Authors and Books
author1 = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author1)
book2 = Book.objects.create(title="No Longer at Ease", author=author1)

author2 = Author.objects.create(name="Ngugi wa Thiong'o")
book3 = Book.objects.create(title="Petals of Blood", author=author2)

# Libraries
library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2, book3)

library2 = Library.objects.create(name="Eastside Library")
library2.books.add(book2, book3)

# Librarians
Librarian.objects.create(name="Grace Mensah", library=library1)
Librarian.objects.create(name="John Mensah", library=library2)

# Users for authentication
User.objects.create_user(username="admin", password="admin123")
User.objects.create_user(username="testuser", password="password")

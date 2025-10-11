import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# --- Optional: Create Sample Data ---
def create_sample_data():
    author, _ = Author.objects.get_or_create(name='Chinua Achebe')
    book1, _ = Book.objects.get_or_create(title='Things Fall Apart', author=author)
    book2, _ = Book.objects.get_or_create(title='No Longer at Ease', author=author)

    library, _ = Library.objects.get_or_create(name='National Library')
    library.books.add(book1, book2)

    librarian, _ = Librarian.objects.get_or_create(name='Mr. Mensah', library=library)

    return author, library, librarian


create_sample_data()


# --- Queries ---

print('\\n1️⃣ All books by a specific author:')
author = Author.objects.get(name='Chinua Achebe')
books = author.books.all()
print([b.title for b in books])

print('\\n2️⃣ All books in a library:')
library = Library.objects.get(name='National Library')
print([b.title for b in library.books.all()])

print('\\n3️⃣ Librarian for a library:')
print(library.librarian.name)

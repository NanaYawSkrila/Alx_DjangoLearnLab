import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    # --- Query 1: All books by a specific author ---
    author_name = "Chinua Achebe"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

    # --- Query 2: List all books in a library ---
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

    # --- Query 3: Retrieve the librarian for a library ---
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

if __name__ == "__main__":
    sample_queries()

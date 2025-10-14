from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

# --- Function-Based View ---
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# --- Class-Based View: Library Details ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all books belonging to this library
        books = self.object.books.all()

        # No category filter since Book model has no category field
        context['books'] = books
        context['book_count'] = books.count()
        return context

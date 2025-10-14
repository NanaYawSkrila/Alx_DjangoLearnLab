from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library, Book

# --- Function-Based View (unchanged) ---
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# --- Class-Based View: Library Details (Enhanced) ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all books belonging to this library
        books = self.object.books.all()

        # Optional: Filter by category if provided in URL query (e.g. ?category=Fiction)
        category = self.request.GET.get('category')
        if category:
            books = books.filter(category__iexact=category)
            context['selected_category'] = category

        # Add useful metadata to the context
        context['books'] = books
        context['book_count'] = books.count()
        context['categories'] = Book.objects.values_list('category', flat=True).distinct()
        return context

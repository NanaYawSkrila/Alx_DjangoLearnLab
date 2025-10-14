from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

# --- Function-Based View: List All Books ---
def list_books(request):
    # Query all books in the database
    books = Book.objects.all()
    # Render them using the correct template path
    return render(request, "relationship_app/list_books.html", {"books": books})


# --- Class-Based View: Library Details ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all books belonging to this library
        books = self.object.books.all()

        # Optional: Filter by category if provided in URL query (only if category exists)
        category = self.request.GET.get("category")
        if hasattr(Book, "category") and category:
            books = books.filter(category__name__iexact=category)
            context["selected_category"] = category

        context["books"] = books
        context["book_count"] = books.count()
        return context

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Library, Book


# --- Function-Based View: List All Books ---
def list_books(request):
    """Displays a list of all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# --- Class-Based View: Library Details (Enhanced) ---
class LibraryDetailView(DetailView):
    """Displays details of a specific library and its associated books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve all books related to this library (assuming related_name='books' in model)
        books = self.object.books.all()
        context['books'] = books
        context['book_count'] = books.count()
        return context


# --- User Registration View ---
def register_view(request):
    """Handles new user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# --- User Login View ---
def login_view(request):
    """Handles user authentication and login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# --- User Logout View ---
def logout_view(request):
    """Logs out the current user."""
    logout(request)
    return render(request, 'relationship_app/logout.html')

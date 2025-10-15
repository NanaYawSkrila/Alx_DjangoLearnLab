cat > relationship_app/views.py <<'PY'
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Library, Book
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


# --- Helper functions to check user roles ---
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- Admin View ---
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# --- Librarian View ---
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# --- Member View ---
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


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
        # Retrieve all books related to this library (expects related_name='books' on M2M)
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
PY




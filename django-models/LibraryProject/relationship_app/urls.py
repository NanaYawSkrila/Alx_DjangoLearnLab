from django.urls import path
from .views import list_books, LibraryDetailView   # ✅ Exact import required

urlpatterns = [
    path('books/', list_books, name='list_books'),  # ✅ Function-based view route
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ Class-based view route
]

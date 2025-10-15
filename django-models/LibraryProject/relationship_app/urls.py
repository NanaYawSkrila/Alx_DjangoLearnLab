from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Function-based view
    path('books/', views.list_books, name='list_books'),

    # Class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('register/', views.register_view, name='register'),  # ✅ matches "views.register"
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ matches "LoginView.as_view(template_name="
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # ✅ matches "LogoutView.as_view(template_name="
]

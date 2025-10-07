from django.contrib import admin
from .models import Author, Book, Library, Librarian


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_filter = ('author',)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('books',)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'library')


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

if __name__ == "__main__":
    print("\nBooks by Author A:")
    for book in get_books_by_author("Author A"):
        print("-", book.title)

    print("\nBooks in Central Library:")
    for book in get_books_in_library("Central Library"):
        print("-", book.title)

    print("\nLibrarian of Central Library:")
    librarian = get_librarian_for_library("Central Library")
    print("-", librarian.name)

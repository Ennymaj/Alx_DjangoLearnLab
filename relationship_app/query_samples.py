# relationship_app/query_samples.py

import os
import sys
import django

# Add the project root (one level above this file) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models_project.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Create sample data
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.set([book1, book2])

    librarian = Librarian.objects.create(name="Alice", library=library)

    # Query all books by a specific author
    print("Books by George Orwell:")
    for book in Book.objects.filter(author__name="George Orwell"):
        print(f"- {book.title}")

    # List all books in a library
    print("\nBooks in Central Library:")
    for book in library.books.all():
        print(f"- {book.title}")

    # Retrieve the librarian for a library
    print("\nLibrarian for Central Library:")
    print(library.librarian.name)

if __name__ == "__main__":
    run_queries()

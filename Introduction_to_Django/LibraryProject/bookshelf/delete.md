# delete.md

```python
from bookshelf.models import Book

book = Book.objects.filter(title="Nineteen Eighty-Four").first()
book.delete()

print(Book.objects.all())

# Output:
# <QuerySet []>

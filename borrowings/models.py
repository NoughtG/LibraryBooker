from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from books.models import Book

class BorrowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)  # ✅ this field MUST exist

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

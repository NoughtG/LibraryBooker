from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BorrowRecord

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "borrow_date", "due_date", "return_date", "returned")
    list_filter = ("returned", "borrow_date", "due_date")
    search_fields = ("user__username", "book__title")

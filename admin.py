from django.contrib import admin

# Register your models here.

#insert reference
from .models import Book
admin.site.register(Book)

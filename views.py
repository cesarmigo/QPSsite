from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def index(request):
    return render(request, 'newhome.html')

def book_by_id(request,book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'Pictures.html', {'book':book})

def contact_us(request):
    return render(request,'contact.html')

def reviews(request):
    return render(request,'review.html')

def gallery(request):
    return render(request, 'newind.html')

def newmain(request):
    return render(request, 'bs4.html')

def next(request):
    return render(request, 'bs3.html')

def ske(request):
    return render(request, 'bootstrap.html')

def skeleton2(request):
    return render(request, 'bs2.html')

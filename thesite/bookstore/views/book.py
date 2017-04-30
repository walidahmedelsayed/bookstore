from django.shortcuts import redirect, render, get_object_or_404
from ..models import Book
from inspect import getmembers
from pprint import pprint

def books(request):
    if not request.user.is_authenticated():
        return redirect('bookstore:login')
    else:
        books = Book.objects.all()
        context = {
            'books': books
        }

        return render(request, 'home.html', context)


def bookdetails(request, id):
    if not request.user.is_authenticated():
        return redirect('bookstore:login')
    else:
        book = get_object_or_404(Book, id=id)

        context = {
            'book': book,
        }
        return render(request, 'bookdetails.html', context)
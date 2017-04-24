# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

from .models import Book, Author

from django.views import generic

from .forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate, login as authlogin, logout


# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'home.html'
#     context_object_name = 'books'
#
#     def get_queryset(self):
#         return Book.objects.all()
#
#
# class BookDetails(generic.DetailView):
#     model = Book
#     template_name = 'bookdetails.html'
#
#
# class AuthorDetails(generic.DetailView):
#     model = Author
#     template_name = 'authordetails.html'
#

def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'home.html', context)


def bookdetails(request, id):
    book = get_object_or_404(Book, id=id)

    context = {
        'book': book,

    }
    return render(request, 'bookdetails.html', context)


def authordetails(request, id):
    author = get_object_or_404(Author, id=id)
    context = {
        'author': author
    }
    return render(request, 'authordetails.html', context)


def register(request):
    if request.method == 'POST':
        return redirect('bookstore:home')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        return redirect('bookstore:home')
    else:
        return render(request, 'login.html')

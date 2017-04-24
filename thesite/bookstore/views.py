# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

from .models import Book, Author, User

from django.contrib.auth.hashers import make_password, check_password

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
        errors = []
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if (name is "" or email is "" or password is "" or repassword is ""):
            errors.append("Please Fill All The Fields")
        elif (password != repassword):
            errors.append("Password Mismatch")

        if (len(errors) > 0):
            return render(request, 'register.html', {'errors': errors})
        else:
            user = User(name=name, email=email, password=make_password(password))
            user.save()
            return redirect('bookstore:home')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        errors = []
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if (user and check_password(password, user.password)):
            return redirect('bookstore:home')
        else:
            errors.append("Invalid Email Or Password")

        if (len(errors) > 0):
            return render(request, 'login.html', {'errors': errors})
        else:
            return redirect('bookstore:home')


    else:
        return render(request, 'login.html')

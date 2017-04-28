# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book , Author
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib.auth.hashers import make_password, check_password
from django.views import generic
# from .forms import RegisterForm, LoginForm

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


def generate_user(name,email,password):
    user = User.objects.create_user(name,email,password)
    return True


def register(request):
    if request.method == 'POST':
        errors = []
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if (username is "" or email is "" or password is "" or repassword is ""):
            errors.append("Please Fill All The Fields")

        elif (password != repassword):
            errors.append("Password Mismatch")

        elif User.objects.filter(username=username).exists():
            errors.append('Username Already Exists With The Same Name')

        elif User.objects.filter(email=email).exists():
            errors.append('Email Already Exists')

        if (len(errors) > 0):
            return render(request, 'register.html', {'errors': errors})
        else:
            if generate_user(username, email, password):
                return redirect('bookstore:home')
            else:
                return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    errors=[]
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            print(user)
            authlogin(request, user)
            return redirect('bookstore:home')
        else:
            errors.append('Invalid UserName or Password')
            return render(request, 'login.html',{'errors':errors})

    else:
        return render(request, 'login.html')



        # if request.method == 'POST':
        #     errors = []
        #     email = request.POST.get('email')
        #     password = request.POST.get('password')
        #     # user = User.objects.get(email=email)
        #     # if (user and check_password(password, user.password)):
        #     #     return redirect('bookstore:home')
        #     # else:
        #     #     errors.append("Invalid Email Or Password")
        #
        #     if (len(errors) > 0):
        #         return render(request, 'login.html', {'errors': errors})
        #     else:
        #         request.session['name'] = 'moustafa'
        #         return redirect('bookstore:home')
        #
        #
        # else:
        #     return render(request, 'login.html')

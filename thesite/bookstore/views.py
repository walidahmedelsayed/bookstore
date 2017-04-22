# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Book, Author

from django.views import generic

from .forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate, login as authlogin, logout


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BookDetails(generic.DetailView):
    model = Book
    template_name = 'bookdetails.html'


class AuthorDetails(generic.DetailView):
    model = Author
    template_name = 'authordetails.html'


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('bookstore:home')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                authlogin(request, user)
                return redirect('bookstore:home')
                print("hello login")
            else:
                return render(request, 'login.html', {'form': form})
                print("faaaaailed")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

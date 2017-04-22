# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Book,Author

from django.views import generic

from .forms import UserForm

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
    form = UserForm()
    return render(request, 'register.html', {'form': form})
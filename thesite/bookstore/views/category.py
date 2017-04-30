from django.shortcuts import redirect, get_object_or_404, render
from ..models import Category, Book


def getCategories(request):
    if not request.user.is_authenticated():
        return redirect('bookstore:login')
    else:
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories.html', context)


def getCategory(request, id):
    if not request.user.is_authenticated():
        return redirect('bookstore:login')
    else:
        category = get_object_or_404(Category, id=id)
        books = Book.objects.all()
        context = {
            'category': category,
            'books': books
        }
        return render(request, 'categorybooks.html', context)

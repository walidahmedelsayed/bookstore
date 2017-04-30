from django.shortcuts import redirect, get_object_or_404, render
from ..models import Category

def getCategories(request):
    categories = Category.objects.all()
    context ={
        'categories': categories
    }
    return render(request,'categories.html',context)
from django.shortcuts import redirect, get_object_or_404, render
from ..models import Author


def authordetails(request, id):
    if not request.user.is_authenticated():
        return redirect('bookstore:login')
    else:
        author = get_object_or_404(Author, id=id)
        context = {
            'author': author
        }
        return render(request, 'authordetails.html', context)
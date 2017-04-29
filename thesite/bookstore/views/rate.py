from django.http.response import JsonResponse
from django.utils.timezone import now

from ..models.rating import Rating


def rate(request):
    print(request.GET['book'])
    rate = Rating.objects.create(rate=request.GET['rating'],
                                 rateDate= now(),
                                 book_id=request.GET['book'],
                                 profile_id=request.user.id
                                 )
    return JsonResponse({'foo': request.user.id},safe=False)

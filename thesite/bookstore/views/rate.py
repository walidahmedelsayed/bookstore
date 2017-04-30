from django.http.response import JsonResponse
from django.utils.timezone import now


from ..models.rating import Rating


def rate(request):
    rate = Rating.objects.filter(book_id=request.GET['book'],profile_id=request.user.id)
    if rate.count() == 0 :
        Rating.objects.create(rate=request.GET['rating'],
                                     rateDate= now(),
                                     book_id=request.GET['book'],
                                     profile_id=request.user.id
                                     )
        return JsonResponse({'res': True}, safe=False)

    else:
        obj = Rating.objects.get(id=rate[0].id)
        obj.rate = request.GET['rating']
        obj.rateDate = now()
        obj.save()
        return JsonResponse({'res': True}, safe=False)

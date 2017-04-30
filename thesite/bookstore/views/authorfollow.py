from django.http.response import JsonResponse
from django.utils.timezone import now


from ..models.authorfollow import AuthorFollow


def follow(request):
    followstatus = AuthorFollow.objects.filter(Author_id=request.GET['author_id'],profile_id=request.user.id)
    followstatus.followStatus = request.GET['followstatus']
    followstatus.update()

    return JsonResponse({'res': True}, safe=False)
    # if rate.count() == 0 :
    #     Rating.objects.create(rate=request.GET['rating'],
    #                                  rateDate= now(),
    #                                  book_id=request.GET['book'],
    #                                  profile_id=request.user.id
    #                                  )
    #     return JsonResponse({'res': True}, safe=False)
    #
    # else:
    #     obj = Rating.objects.get(id=rate[0].id)
    #     obj.rate = request.GET['rating']
    #     obj.rateDate = now()
    #     obj.save()
    #     return JsonResponse({'res': True}, safe=False)


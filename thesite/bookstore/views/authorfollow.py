from django.http.response import JsonResponse
from django.utils.timezone import now

from ..models.authorfollow import AuthorFollow


def follow(request):
    followstatus = AuthorFollow.objects.filter(Author_id=request.GET['author_id'], profile_id=request.user.id)

    if followstatus.count() == 0:
        AuthorFollow.objects.create(followStatus=request.GET['followstatus'],
                              Author_id=request.GET['book'],
                              profile_id=request.user.id
                              )
        return JsonResponse({'res': True}, safe=False)

    else:
        obj = AuthorFollow.objects.get(id=followstatus[0].id)
        print(request.GET.get('followstatus'))
        if obj.followStatus == 0  :
            obj.followStatus = 1
            obj.save()
        else:
            obj.followStatus = 0
            obj.save()

        return JsonResponse({'res': True}, safe=False)

from django.http.response import JsonResponse
from django.utils.timezone import now
from django.shortcuts import redirect
from ..models.authorfollow import AuthorFollow


def follow(request):
    if not request.user.is_authenticated():
        return redirect('bookstore:login')
    else:
        followstatus = AuthorFollow.objects.filter(Author_id=request.GET['author'], profile_id=request.user.id)

        if followstatus.count() == 0:
            AuthorFollow.objects.create(followStatus=request.GET['status'],
                                  Author_id=request.GET['author'],
                                  profile_id=request.user.id
                                  )

            return JsonResponse({'follow': True}, safe=False)

        else:
            obj = AuthorFollow.objects.get(id=followstatus[0].id)
            if obj.followStatus == 0:
                obj.followStatus = 1
                obj.save()
                return JsonResponse({'follow': True}, safe=False)
            else:
                obj.followStatus = 0
                obj.save()
                return JsonResponse({'follow': False}, safe=False)

from django.http.response import JsonResponse
from django.utils.timezone import now

from ..models import Status


def read(request):
    read = Status.objects.filter(book_id=request.GET['book'],profile_id=request.user.id)
    if read.count() == 0 :
        Status.objects.create(status=request.GET['status'],
                                     date= now(),
                                     book_id=request.GET['book'],
                                     profile_id=request.user.id
                                     )

        return JsonResponse({'read': True}, safe=False)
    else:
        obj = Status.objects.get(id=read[0].id)
        if obj.status == 1:
            obj.status = 2
            obj.date = now()
            obj.save()
            return JsonResponse({'read': True}, safe=False)
        else:
            obj.status = 1
            obj.date = now()
            obj.save()
        return JsonResponse({'read': False}, safe=False)

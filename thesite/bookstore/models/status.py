from django.db import models


class Status(models.Model):
    UNREAD_STATUS = 1
    READ_STATUS = 2
    WISH_STATUS = 3
    STATUS_CHOICES = (
        (UNREAD_STATUS, 'not read'),
        (READ_STATUS, 'readed'),
        (WISH_STATUS, 'wish'),
    )
    book = models.ForeignKey("Book", on_delete=models.CASCADE,default=1)
    profile = models.ForeignKey("Profile",related_name="statusProfile",  on_delete=models.CASCADE,default=1)
    status = models.IntegerField(choices=STATUS_CHOICES, default=UNREAD_STATUS)
    date = models.DateField(default=0)
from django.db import models


class Rating(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE,default=1)
    profile = models.ForeignKey("Profile",related_name="ratingProfile",  on_delete=models.CASCADE,default=1)
    rate = models.IntegerField()
    rateDate = models.DateField(default=0)
from django.db import models

class AuthorFollow(models.Model):
    Author = models.ForeignKey("Author", on_delete=models.CASCADE, default=1)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, default=1)
    followStatus = models.IntegerField(default=0)

    def __str__(self):
        return self.followStatus

    def get_follow_status(self):
        print (self)
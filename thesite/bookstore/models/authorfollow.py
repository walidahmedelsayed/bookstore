from django.db import models

class AuthorFollow(models.Model):
    Author = models.ForeignKey("Author", on_delete=models.CASCADE, default=1)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, default=1)
    followStatus = models.BooleanField(default=0)

    def __str__(self):
        return self.followStatus
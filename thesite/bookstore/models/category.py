from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


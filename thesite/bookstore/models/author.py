from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    born_at = models.DateField(blank=True)
    died_at = models.DateField(blank=True, null=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

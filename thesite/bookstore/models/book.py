from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    published_at = models.DateField(blank=True)
    summary = models.CharField(max_length=600)
    img = models.ImageField(upload_to='images/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, default=1)
    profileRating = models.ManyToManyField("Profile",related_name="rating", through='Rating')
    profileStatus = models.ManyToManyField("Profile",related_name="status",  through='Status')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


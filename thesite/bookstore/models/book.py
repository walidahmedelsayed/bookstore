from urllib import request

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

    def get_due_date_string(self):
        fiveStar = 0
        fourStar = 0
        threeStar = 0
        twoStar = 0
        oneStar = 0
        for rate in self.rating_set.all():
            if rate.rate == 5:
                fiveStar += 1
            elif rate.rate ==4:
                fourStar += 1
            elif rate.rate == 4:
                threeStar += 1
            elif rate.rate == 4:
                twoStar += 1
            else:
                oneStar += 1
        rating = ((5 * fiveStar) + (4*fourStar) + (3*threeStar) + (2*twoStar) + (1*oneStar)) / (fiveStar+fourStar+threeStar+threeStar+oneStar)
        #print(rating)
        return self.name
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author', through='AuthorFollow')
    categories = models.ManyToManyField('Category')
    booksRating = models.ManyToManyField("Book",related_name="booksRating", through='Rating')
    booksStatus = models.ManyToManyField("Book",related_name="booksStatus",  through='Status')


    def __str__(self):
        return self.user.email


# Synchronizing User model with Profile model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
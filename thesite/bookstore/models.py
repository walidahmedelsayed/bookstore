# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver

from django.contrib.auth.models import User

from datetime import datetime

from django.utils.timezone import now

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=100, blank=False)
#     password = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    born_at = models.DateField(blank=True)
    died_at = models.DateField(blank=True, null=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    published_at = models.DateField(blank=True)
    summary = models.CharField(max_length=600)
    img = models.ImageField(upload_to='images/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, default=1)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')
    categories = models.ManyToManyField('Category')
    books = models.ManyToManyField('Book', through='Rate')

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


class Rate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    STATES = [('read', 'Read'), ('wish', 'Wish'),('none','None')]
    state = models.CharField(max_length=10, choices=STATES, default='none')
    RATES = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")]
    rate = models.CharField(max_length=2, choices=RATES)

    def __str__(self):
        return self.rate

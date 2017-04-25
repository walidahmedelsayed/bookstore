# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime


# Create your models here.
from django.utils.timezone import now


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    born_at = models.DateField(blank=True)
    died_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    published_at = models.DateField(blank=True)
    summary = models.CharField(max_length=600)
    img = models.ImageField(upload_to = 'images/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
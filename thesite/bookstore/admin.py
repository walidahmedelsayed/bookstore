# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User,Book,Author,Categories

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Categories)

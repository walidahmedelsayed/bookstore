# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20170425_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

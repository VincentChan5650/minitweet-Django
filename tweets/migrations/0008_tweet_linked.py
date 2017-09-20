# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-27 07:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0007_tweet_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='linked',
            field=models.ManyToManyField(blank=True, related_name='linked', to=settings.AUTH_USER_MODEL),
        ),
    ]
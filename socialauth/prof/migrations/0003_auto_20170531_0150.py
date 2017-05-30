# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_auto_20170529_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='locale',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True),
        ),
    ]

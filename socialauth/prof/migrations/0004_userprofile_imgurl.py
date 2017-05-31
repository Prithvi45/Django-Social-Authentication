# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_auto_20170531_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='imgurl',
            field=models.URLField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesi', '0002_lecture_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='note',
            name='image',
        ),
        migrations.AddField(
            model_name='lecture',
            name='date',
            field=models.CharField(default='2014-10-18', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='image_url',
            field=models.URLField(default='https://i.imgur.com/GB6nntt.png'),
            preserve_default=False,
        ),
    ]

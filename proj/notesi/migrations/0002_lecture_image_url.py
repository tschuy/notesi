# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='image_url',
            field=models.URLField(default='https://i.imgur.com/GB6nntt.png'),
            preserve_default=False,
        ),
    ]

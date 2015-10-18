# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesi', '0004_auto_20151018_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='image_url',
        ),
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(default='asdf.jpg', upload_to=b''),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesi', '0003_auto_20151018_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='date',
            field=models.DateField(),
        ),
    ]

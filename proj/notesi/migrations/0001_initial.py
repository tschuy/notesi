# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('professor', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('department', models.CharField(max_length=10)),
                ('course_code', models.CharField(max_length=10)),
                ('term', models.CharField(max_length=10, choices=[(b'FALL', b'Fall'), (b'WINTER', b'Winter'), (b'SUMMER', b'Summer'), (b'SPRING', b'Spring')])),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='notesi.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_count', models.IntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('lecture', models.ForeignKey(to='notesi.Lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('courses', models.ManyToManyField(to='notesi.Course')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('acronym', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='univerities',
            field=models.ManyToManyField(to='notesi.University'),
        ),
        migrations.AddField(
            model_name='note',
            name='student',
            field=models.ForeignKey(to='notesi.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(to='notesi.University'),
        ),
        migrations.AddField(
            model_name='campus',
            name='university',
            field=models.ForeignKey(to='notesi.University'),
        ),
    ]

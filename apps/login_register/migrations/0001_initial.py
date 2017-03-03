# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userLevel', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=45)),
                ('lastname', models.CharField(default='poopyhead', max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

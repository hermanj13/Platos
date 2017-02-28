# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_register', '0002_auto_20170228_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('about_me', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='login_register.User')),
            ],
        ),
    ]
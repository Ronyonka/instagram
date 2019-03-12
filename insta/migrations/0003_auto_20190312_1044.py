# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 07:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
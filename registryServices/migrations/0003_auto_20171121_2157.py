# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 21:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registryServices', '0002_auto_20171121_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='registry',
            name='name',
            field=models.CharField(default='NewRegistry', max_length=200),
        ),
        migrations.AlterField(
            model_name='registryitem',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.IntegerField()),
                ('item_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=200)),
                ('colour', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='registryitem',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryServices.User'),
        ),
        migrations.AddField(
            model_name='registryitem',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryServices.Item'),
        ),
        migrations.AddField(
            model_name='registryitem',
            name='registry_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryServices.Registry'),
        ),
        migrations.AddField(
            model_name='registry',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryServices.User'),
        ),
    ]
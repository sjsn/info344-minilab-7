# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('summary', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=65)),
                ('link', models.URLField(max_length=100)),
                ('img', models.URLField(max_length=100)),
                ('author', models.ManyToManyField(to='books_api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(to='books_api.Publisher'),
        ),
    ]

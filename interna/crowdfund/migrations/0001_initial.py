# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='What do you want to fund?', max_length=80)),
                ('short_description', models.CharField(help_text='Describe your project in 300 characters', max_length=300)),
                ('long_description', models.TextField(help_text='Describe your project in more detail')),
                ('amount_required', models.PositiveIntegerField(help_text='How many CHF does this project need to be funded?')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When was this funding project launched?')),
            ],
            options={
                'ordering': ('-created', 'title'),
            },
        ),
    ]

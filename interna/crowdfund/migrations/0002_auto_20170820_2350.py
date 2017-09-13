# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfund', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='', help_text='A photo showing your project', upload_to='crowdfund_projects/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.CharField(help_text='Describe your project in 300 characters or less', max_length=300),
        ),
    ]
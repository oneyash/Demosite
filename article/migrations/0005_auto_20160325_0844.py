# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160321120913 on 2016-03-25 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_articles_image_small'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publication_date',
            field=models.DateField(db_index=True, null=True),
        ),
    ]

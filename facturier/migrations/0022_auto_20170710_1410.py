# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0021_auto_20170710_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='date_validation',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

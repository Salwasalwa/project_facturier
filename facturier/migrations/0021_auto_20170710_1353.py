# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 13:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0020_facture_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='date_facturation',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='facture',
            name='date_validation',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]

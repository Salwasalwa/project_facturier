# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0014_auto_20170703_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(choices=[('progress', 'In progress'), ('refuse', 'Refuse'), ('win', 'To win')], max_length=2),
        ),
    ]

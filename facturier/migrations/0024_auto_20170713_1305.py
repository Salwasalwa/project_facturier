# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0023_auto_20170713_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devis',
            name='compte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.Compte'),
        ),
    ]
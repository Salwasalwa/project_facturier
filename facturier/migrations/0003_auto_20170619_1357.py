# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0002_facture_devis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive',
            name='devis',
        ),
        migrations.DeleteModel(
            name='Archive',
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models import CharField, Model
from autoslug import AutoSlugField
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.

class Compte(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    adress = models.CharField(verbose_name='adress', max_length=100, null=True, blank=True)
    zipcode = models.IntegerField(verbose_name='zipcode', null=True, blank=True )
    city = models.CharField(verbose_name='city', max_length=50, null=True, blank=True )
    email_contact = models.CharField(verbose_name='email contact', max_length=100, null=True, blank=True )

    def __unicode__(self):
        return self.user.username

class Client(models.Model):
    name =  models.CharField(verbose_name='name', max_length=100)
    prenom =  models.CharField(verbose_name='prénom', max_length=100)
    adress = models.CharField(verbose_name='adress', max_length=100, null=True, blank=True)
    zipcode = models.IntegerField(verbose_name='zipcode', null=True, blank=True )
    city = models.CharField(verbose_name='city', max_length=50, null=True, blank=True )
    email_contact = models.CharField(verbose_name='email contact', max_length=100, null=True, blank=True )
    slug = AutoSlugField(populate_from='name', unique_with='name')

    def __unicode__(self):
        return self.name

class Devis(models.Model):
    STATUS = (
    ('progress', 'In progress'),
    ('refuse', 'Refuse'),
    ('win', 'To win')
    )
    title = models.CharField(verbose_name='title', max_length=100)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    date_creation = models.DateTimeField( null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True)
    compte = models.ForeignKey(Compte, null=True, blank=True)
    client = models.ForeignKey(Client)
    status = models.CharField(max_length=50, choices=STATUS)
    montant = models.IntegerField(verbose_name='montant', null=True, blank=True )

    def __unicode__(self):
        return self.title

class LigneDevis(models.Model):
    descpt = models.CharField(verbose_name='descpt', max_length=200)
    prix = models.IntegerField(verbose_name='prix', null=True, blank=True)
    qty = models.IntegerField(verbose_name='qty', null=True, blank=True)
    devis = models.ForeignKey(Devis)

class Facture(models.Model):
    STATUS = (
    ('1', 'In progress'),
    ('2', 'paid')
    )
    title = models.CharField(verbose_name='title', max_length=100)
    date_facturation = models.DateTimeField(null=True, blank=True)
    date_validation = models.DateTimeField( null=True, blank=True)
    devis = models.ForeignKey(Devis, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS)

    def __unicode__(self):
        return self.title

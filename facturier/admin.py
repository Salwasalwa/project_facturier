# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from models import *

class CompteAdmin(admin.ModelAdmin):
    model = Compte

admin.site.register(Compte, CompteAdmin)


class LigneDevisInline(admin.TabularInline):
    model = LigneDevis

class DevisAdmin(admin.ModelAdmin):
    inlines = [
        LigneDevisInline,
    ]

admin.site.register(Devis, DevisAdmin)
admin.site.register(LigneDevis)


class FactureAdmin(admin.ModelAdmin):
    model = Facture
    verbose_name_plural = 'Facture'

admin.site.register(Facture, FactureAdmin)

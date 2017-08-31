from django import forms
from django.forms import inlineformset_factory
from models import *


DevisInlineFormset = inlineformset_factory(Devis, LigneDevis, fields="__all__", min_num=1, extra=1)

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = "__all__"

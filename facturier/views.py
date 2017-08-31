# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from autoslug import AutoSlugField
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from forms import *
# Create your views here.
def homepage(request):
    return render(request, "homepage.html")


# def devis_detail(request, slug):
#     devis = Devis.objects.get(slug=slug)
#
#     context = {
#         "devis" : devis
#     }
#
#     return render(request, "facturier/devis_detail.html", context)

class DevisDetailView(DetailView):
    model = Devis
    slug_field = "slug"
    template_name = 'facturier/devis_detail.html'

class DevisUpdateView(UpdateView):
    model = Devis
    fields = "__all__"
    template_name = 'facturier/devis_edit.html'
    success_url = reverse_lazy("list_devis")

    def get_context_data(self):
        context = UpdateView.get_context_data(self)
        context["devis_formset"] = DevisInlineFormset(instance=self.object)
        return context

    def form_valid(self, form):
        devis_resp = UpdateView.form_valid(self, form)
        devis_formset = DevisInlineFormset(self.request.POST, instance=self.object)

        if devis_formset.is_valid():
            devis_formset.save()
        else:
            print devis_formset.errors

        return devis_resp


class DevisCreateView(CreateView):
    model = Devis
    fields = "__all__"
    success_url = "devis/create"

    def get_context_data(self):
        context = CreateView.get_context_data(self)
        context["devis_formset"] = DevisInlineFormset()
        return context

    def form_valid(self, form):
        devis_resp = CreateView.form_valid(self, form)
        devis_formset = DevisInlineFormset(self.request.POST, instance=self.object)

        if devis_formset.is_valid():
            devis_formset.save()


        return devis_resp

    def get_success_url(self):
        return reverse('list_client')

class DevisListView(ListView):
    model = Devis
    context_object_name = "deviss"
    template_name = 'list_devis.html'


def client_detail(request, slug):
    client = Client.objects.get(slug=slug)

    context = {
        "client" : client
    }

    return render(request, "facturier/client_detail.html", context)

class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    template_name = 'facturier/client_edit.html'
    success_url = "/list/clients"

class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"
    success_url = "/client/create"

class ClientListView(ListView):
    model = Client
    context_object_name = "clients"
    template_name = 'client_list.html'

class FactureListView(ListView):
    model = Facture
    context_object_name = "factures"
    template_name = 'facture_list.html'

class FactureCreateView(CreateView):
    model = Facture
    fields = "__all__"
    success_url = reverse_lazy("list_facture")

    def get_initial(self):
        if self.request.method == "GET":
            initial = {
                "devis" : Devis.objects.get(id=self.request.GET["devis_id"]),
                "status" : "1"
            }
            return initial
        else:
            return {}


class StatusUpdateView(UpdateView):
    model = Devis
    fields = "status"

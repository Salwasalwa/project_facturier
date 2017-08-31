from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', homepage, name="home"),

    url(r'^list/clients$', ClientListView.as_view(), name="list_client"),
    url(r'^client/create$', ClientCreateView.as_view(), name='create-client'),
    url(r'^client/(?P<slug>[\w-]+)$', client_detail, name="client-detail"),
    url(r'^client/(?P<slug>[\w-]+)/edit$', ClientUpdateView.as_view(), name="client-edit"),


    url(r'^devis/create$', DevisCreateView.as_view(), name='create-devis'),
    url(r'^list/devis$', DevisListView.as_view(), name="list_devis"),
    url(r'^devis/(?P<slug>[\w-]+)$', DevisDetailView.as_view(), name="devis-detail"),
    url(r'^devis/(?P<slug>[\w-]+)/edit$', DevisUpdateView.as_view(), name="devis-edit"),

    url(r'^devis/(?P<slug>[\w-]+)/refuse$', StatusUpdateView.as_view(), name='status-edit'),

    url(r'^facture/create$', FactureCreateView.as_view(), name="create-facture"),

    url(r'^facture/list$', FactureListView.as_view(), name="list_facture"),

    # url(r'^devis/(?P<slug>[\w-]+)$', DevisDetailView.as_view, name="devis-detail"),

]

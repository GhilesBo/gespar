from django.urls import path
from gespar import views

urlpatterns = [
    path('', views.index, name='index'),
    path('commande/', views.commande_form, name='commande_form'),
    path('renseignement_vh_fils/', views.renseignement_vh_fils_form, name='renseignement_vh_fils_form'),
    path('renseignement_vh_pere/', views.renseignement_vh_pere_form, name='renseignement_vh_pere_form'),
    path('etude_technique/', views.etude_technique_form, name='etude_technique_form'),
    path('livraison/', views.livraison_form, name='livraison_form'),
]

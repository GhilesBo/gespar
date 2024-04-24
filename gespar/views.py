# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from gespar.forms import CommandeForm, RenseignementVhFilsForm, RenseignementVhPereForm, EtudeTechniqueForm, LivraisonForm

def index(request):
    return render(request, 'index.html')

def commande_form(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic for redirection after form submission here
    else:
        form = CommandeForm()
    return render(request, 'commande_form.html', {'form': form})

def renseignement_vh_fils_form(request):
    if request.method == 'POST':
        form = RenseignementVhFilsForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic for redirection after form submission here
    else:
        form = RenseignementVhFilsForm()
    return render(request, 'rens_vh_fils_form.html', {'form': form})

def renseignement_vh_pere_form(request):
    if request.method == 'POST':
        form = RenseignementVhPereForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic for redirection after form submission here
    else:
        form = RenseignementVhPereForm()
    return render(request, 'rens_vh_père_form.html', {'form': form})

def etude_technique_form(request):
    if request.method == 'POST':
        form = EtudeTechniqueForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic for redirection after form submission here
    else:
        form = EtudeTechniqueForm()
    return render(request, 'etude_technique_form.html', {'form': form})

def livraison_form(request):
    if request.method == 'POST':
        form = LivraisonForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic for redirection after form submission here
    else:
        form = LivraisonForm()
    return render(request, 'livraison_form.html', {'form': form})

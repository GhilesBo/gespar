from django import forms
from .models import Commande, RenseignementVhPere, RenseignementVhFils, EtudeTechnique, Livraison

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Specify which fields are required
            required_fields = ['pk_NumeroCommande', 'Annee', 'Budget', 'Financement', 'TypeVehicule', 'Categorie', 'Designation', 'EtatSignatureCommandeAchat']
            for field_name, field in self.fields.items():
                if field_name in required_fields:
                    field.required = True

class RenseignementVhPereForm(forms.ModelForm):
    class Meta:
        model = RenseignementVhPere
        fields = '__all__'

class RenseignementVhFilsForm(forms.ModelForm):
    class Meta:
        model = RenseignementVhFils
        fields = '__all__'

class EtudeTechniqueForm(forms.ModelForm):
    class Meta:
        model = EtudeTechnique
        fields = '__all__'

class LivraisonForm(forms.ModelForm):
    class Meta:
        model = Livraison
        fields = '__all__'

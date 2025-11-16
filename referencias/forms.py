

from django import forms
from .models import Referencias, Pensamientos


########################

class PensamientosForm(forms.ModelForm):
    class Meta:
        model = Pensamientos
        fields = ['nombre','descripcion', 'etiquetas']
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple(),
        }

class ReferenciasForm(forms.ModelForm):
    class Meta:
        model = Referencias
        fields = ['nombre', 'autor','descripcion', 'etiquetas']
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple(),
        }

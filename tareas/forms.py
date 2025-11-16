from django import forms
from django.utils.timezone import now
from tareas.models import Tarea
from etiquetas.models import Etiqueta

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'tipo', 'proximidad', 'prioridad', 'etiquetas', 'fecha_termino']
        widgets = {
            'etiquetas': forms.CheckboxSelectMultiple(),
            'fecha_termino': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control', 'min': now().strftime("%Y-%m-%dT%H:%M")}
            ),
        }

    def clean_fecha_termino(self):
        fecha = self.cleaned_data.get('fecha_termino')
        if fecha and fecha <= now():
            raise forms.ValidationError("La fecha de término debe estar en el futuro.")
        return fecha

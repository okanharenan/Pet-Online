from django import forms
from .models import ReservaModel

class ReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaModel
        fields = ['nome', 'email', 'nome_pet', 'data', 'turno', 'tamanho', 'observacoes']

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
from django import forms
from .models import ContatoModel


class ContatoForms(forms.ModelForm):
    class Meta:
        model = ContatoModel
        fields = ['nome', 'telefone', 'email', 'mensagem']

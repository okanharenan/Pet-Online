from django import forms
from .models import ReservaModel
from datetime import date
from django.core.exceptions import ValidationError

class ReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaModel
        fields = '__all__'

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError("Data inválida. Tente colocar uma data atual.")
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        data_atual = cleaned_data.get('data')

        if data_atual:
            agendamento_dia = ReservaModel.objects.filter(data=data_atual).count()
            maximo_agendamento = 4

            if agendamento_dia >= maximo_agendamento:
                raise forms.ValidationError("Limite de agendamento por dia atingido. Tente agendar para outro dia!")

        return cleaned_data

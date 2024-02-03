from django import forms
from .models import ReservaModel
from datetime import date
from django.core.exceptions import ValidationError

class ReservaForm(forms.ModelForm):
    
    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError("Data inválida tente colocar uma data atual")
        return data

    

    '''   def clean(self):
         clean_data = super().clean()
         data_atual = self.cleaned_data.get('data')

         if data_atual:
              agendamento_dia = ReservaModel.objects.all().count()
              maximo_agendamento = 4

              if agendamento_dia > maximo_agendamento:
                   self.add_error('data','Limite de agendamento por dia atingido tente agendar para outro dia!')
         return clean_data'''
     
    class Meta:
        model = ReservaModel
        fields = '__all__'

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }




       
from django.db import models

#modelo reservas

class ReservaModel(models.Model):

    TURNO = (
        ('manhã','Manhã'),
        ('tarde','Tarde')

    )

    TAMANHO_PET=(
        (0,'Pequeno'),
        (1,'Médio'),
        (2,'Grande')
    )

    nome = models.CharField(verbose_name="Nome", max_length=50)
    email = models.EmailField(verbose_name="E-mail")
    nome_pet = models.CharField(verbose_name="Nome do Pet", max_length=50)
    data = models.DateField(verbose_name="Data", help_text="dd/mm/aaaa")
    turno = models.CharField(verbose_name="Turno", max_length=10, choices=TURNO)
    tamanho =models.IntegerField(verbose_name="Tamanho", choices = TAMANHO_PET)
    observacoes = models.TextField(verbose_name="Observações", blank=True)

  
from django.db import models

# create Models Contato

class ContatoModel(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50)
    telefone = models.CharField(verbose_name="Telefone", max_length=12)
    email = models.EmailField(verbose_name='E-mail')
    mensagem = models.TextField(verbose_name="Mensagem")
    data = models.DateTimeField(verbose_name="Data Envio", auto_now_add=True)

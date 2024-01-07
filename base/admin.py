from django.contrib import admin
from django.contrib import messages
from base.models import ContatoModel

@admin.action(description="Marcar formulário como lido")
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message.user(request, 'Formulario de contato(s) marcado como lido', messages.SUCCESS)


@admin.register(ContatoModel)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'data' , 'lido']
    search_fields=['nome','telefone','email']
    list_filter=['data','lido']
    actions = [marcar_como_lido]


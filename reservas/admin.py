from django.contrib import admin
from .models import ReservaModel

# Register your models here.
@admin.register(ReservaModel)
class ResevaAdmin(admin.ModelAdmin):
    pass
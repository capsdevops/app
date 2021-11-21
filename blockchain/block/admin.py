from django.contrib import admin

from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ["subject", "__str__", "message"]


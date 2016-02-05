from django.contrib import admin
from .models import *
from .export_utils import export_xls

class InscriptionAdmin(admin.ModelAdmin):
    actions = [export_xls]

admin.site.register(Inscription,InscriptionAdmin)

from django.contrib import admin
from services import models

# Registrar los modelos que agregamos en la base de datos para que puedan ser usados en el panel de admin
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('-updated',)
    search_fields = ('title',)
    
admin.site.register(models.Services, ServicesAdmin)

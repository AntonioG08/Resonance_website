from django.db import models


# Usado para crear los modelos de la base de datos
class Services(models.Model):
    title = models.CharField(max_length=60, null=False, verbose_name='Título del servicio')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-updated']
    
    # Used to show a best 'title' or 'Placeholder' of the model in the admin tab/view
    def __str__(self):
        return self.title
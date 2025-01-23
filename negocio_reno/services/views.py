from django.shortcuts import render
from django.views.generic import View, ListView
from services import models #Usado para importar todos los modelos de la app 'Services' 


#Clase utilizada para cargar el template 'gallery.html' donde se muestran los servicios del negocio
class Gallery(ListView):
    template_name = 'services/gallery.html'
    model = models.Services
    context_object_name = 'servicios'
    
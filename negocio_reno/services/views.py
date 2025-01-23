from django.shortcuts import render
from django.views.generic import View


#Clase utilizada para cargar el template 'gallery.html' donde se muestran los servicios del negocio
class Gallery(View):
    def get(self, request):
        return render(request, 'services/gallery.html')
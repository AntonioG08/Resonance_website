from django.urls import path
from services import views #IMPORTANTE importar las vistas de la misma app y no de otra


app_name = 'services'
urlpatterns = [
    path('gallery-&-services/', views.Gallery.as_view(), name='gallery'), #URL usado para la página de galería y servicios
]

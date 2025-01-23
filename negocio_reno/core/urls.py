from django.urls import path
from core import views #IMPORTANTE importar las vistas de la misma app y no de otra


app_name = 'core'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about-us/', views.Us.as_view(), name='us'),
]

from django.urls import path
from contact import views #IMPORTANTE importar las vistas de la misma app y no de otra


app_name = 'contact'
urlpatterns = [
    path('', views.Contact_us.as_view(), name='contact-us'),
]
from django.urls import path
from registration import views #IMPORTANTE importar las vistas de la misma app y no de otra


app_name = 'registration'
urlpatterns = [
    path('', views.LogIntoAdmin.as_view(), name='new_admin_login')
]

from django.urls import path
from registration import views


app_name = 'registration'
urlpatterns = [
    path('', views.LogIntoAdmin.as_view(), name='new_admin_login')
]

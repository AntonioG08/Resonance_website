from django.urls import path
from core import views


app_name = 'core'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about-us/', views.Us.as_view(), name='us'),
    path('gallery-&-services/', views.Gallery.as_view(), name='gallery'),
]

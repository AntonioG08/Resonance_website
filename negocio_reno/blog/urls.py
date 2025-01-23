from django.urls import path
from blog import views #IMPORTANTE importar las vistas de la misma app y no de otra


app_name = 'blog'
urlpatterns = [
    path('reviews/', views.Reviews.as_view(), name='reviews'),
    path('events/', views.Events.as_view(), name='events'),
]
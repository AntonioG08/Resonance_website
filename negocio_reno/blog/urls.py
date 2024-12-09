from django.urls import path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('reviews/', views.Reviews.as_view(), name='reviews'),
]
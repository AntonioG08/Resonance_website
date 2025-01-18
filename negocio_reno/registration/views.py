from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.
class LogIntoAdmin(LoginView):
    template_name = 'registration/login_admin.html'
    next_page = reverse_lazy('admin:index')
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

#View based on classes used to log into the admin panel (personalized)
class LogIntoAdmin(LoginView):
    template_name = 'registration/login_admin.html' #Personalized templates, I'm aware Django offers one but I wanted a personalized one
    next_page = reverse_lazy('admin:index') #Reverse lazy function used to move the user to the main page of the admin onced logged in
    redirect_authenticated_user=True #In case the users leaves, but is still logged in, it can be redirected automatically
    
    """Note: Need to implement the functionality of kicking out the user after a determined amount of time, for example, if the user 
    logged 1 hour ago, and went to eat, or just started doing something else and didn't logged out, then the system will kick him out. 
    Preferently, lets do this based on inactivity, I've found this link that might be useful or have the solution:
    https://stackoverflow.com/questions/31670231/autologout-a-user-after-specific-time-in-django """

from django.shortcuts import render
from django.views.generic import View

# Create your views here.

#Class used to render the 'home' template which is the main page
class Home(View):
    def get(self, request):
        return render(request, 'core/home.html')


#Class used to render the 'Us' template which contains information about us
class Us(View):
    def get(self, request):
        return render(request, 'core/us.html')


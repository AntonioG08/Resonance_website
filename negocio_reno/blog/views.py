from django.shortcuts import render
from django.views.generic import View

# Create your views here.

#Class used to render the 'Review' template which is the main page
class Reviews(View):
    def get(self, request):
        return render(request, 'blog/reviews.html')


#Class used to render the 'Events' template which is the main page
class Events(View):
    def get(self, request):
        return render(request, 'blog/events.html')
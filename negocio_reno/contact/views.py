from django.shortcuts import render
from django.views.generic import View


#Class used to render the 'Contact_us' templates used for the contact page
class Contact_us(View):
    def get(self, request):
        return render(request, 'contact/contact_us.html')


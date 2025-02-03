"""
URL configuration for negocio_reno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('accounts/', include('registration.urls')),
    path('admin-resonance-users-only-restricted/', admin.site.urls, name='admin'), #Used to enter to the admin panel
    path('admin-resonance-users-only/', include('registration.urls')), #Used to modify and personalize the admin login view
    path('', include('core.urls')), #Used to import all the URLs paths of 'Core'
    path('blog/', include('blog.urls')), #Used to import all the URLs paths of 'Blog'
    path('services/', include('services.urls')), #Used to import all the URLs paths of 'Services'
    path('contact-us/', include('contact.urls')) #Used to import all the URLs paths of 'Contact'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

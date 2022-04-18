"""initial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.shortcuts import render

# UARPA == UA Refugee Photo Accounting
admin.site.site_title = "UARPA Admin" # appears at the top of the browser window when admin tab is active
admin.site.site_header = "UARPA Credentials"  # appears above username/password dialog
admin.site.index_title = "Welcome to UARPA" # dunno where

def home(request):
  context = {
    'is_photographer': request.user.groups.filter(name='photographer').exists()
    ,'is_staff': request.user.groups.filter(name='staff').exists()
  }
  return render(request ,'home.html' ,context)

urlpatterns = [
    path('admin/', admin.site.urls)
    ,path('accounts/', include('django.contrib.auth.urls'))
    ,path('photo_accounting/', include('photo_accounting.urls'))
    ,path('', home, name='home')
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


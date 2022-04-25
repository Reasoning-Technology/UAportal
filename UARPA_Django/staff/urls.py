from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
  path('photographer/' ,views.photographer ,name='staff_photographer')
  ,path('refugee/' ,views.refugee ,name='staff_refugee')
  ,path('refugee_print_QR/<str:rid>/' ,views.refugee_print_QR ,name='refugee_print_QR')
]

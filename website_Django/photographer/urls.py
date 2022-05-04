from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
  path('log/<str:rid>' ,views.log ,name='photographer_log')
]

from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
  path('', views.index, name='index')
  ,path('photo_taken/', views.PhotoTakenView.as_view(), name='photo_taken')
  ,path('accounts/', include('django.contrib.auth.urls'))
]

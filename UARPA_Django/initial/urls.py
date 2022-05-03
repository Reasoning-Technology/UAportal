from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import *

# UARPA == UA Refugee Photo Accounting
admin.site.site_title = "UARPA Admin" # appears at the top of the browser window when admin tab is active
admin.site.site_header = "UARPA Credentials"  # appears above username/password dialog
admin.site.index_title = "Welcome to UARPA" # dunno where

urlpatterns = [
#    path('admin/' ,admin.site.urls)
     path('audit/' ,admin.site.urls)
    ,path('accounts/' ,include('django.contrib.auth.urls'))
    ,path('photographer/' ,include('photographer.urls'))
    ,path('organizer/' ,include('organizer.urls'))
    ,path('' ,initial ,name='initial')
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


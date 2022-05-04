from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import *

admin.site.site_title = "UAportal Admin" # appears at the top of the browser window when admin tab is active
admin.site.site_header = "UAportal Credentials"  # appears above username/password dialog
admin.site.index_title = "Welcome to UAportal" # dunno where

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


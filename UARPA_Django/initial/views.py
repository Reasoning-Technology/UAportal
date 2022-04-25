from django.views.generic import RedirectView
from django.shortcuts import render

def initial(request):
  context = {
    'is_photographer': request.user.groups.filter(name='photographer').exists()
    ,'is_staff': request.user.groups.filter(name='staff').exists()
  }
  return render(request ,'initial.html' ,context)


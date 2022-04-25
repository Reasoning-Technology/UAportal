from django.shortcuts import render

# Create your views here.

def index(request):
  context = {
    'num_books': 5
    ,'num_instances': 10
    ,'num_instances_available': 15
    ,'num_authors': 20
  }
  return render(request, 'index.html', context=context)

from django.views import generic
from shared.models import PhotoTaken

class PhotoTakenView(generic.ListView):
  model = PhotoTaken
  # default is without underscores: template_name = 'photo_accounting/phototaken_list.html'
  # requires the '.html' suffix
  # found in photo_accounting/templates/photo_accounting/photo_taken_list.html
  template_name = 'photo_accounting/photo_taken_list.html'

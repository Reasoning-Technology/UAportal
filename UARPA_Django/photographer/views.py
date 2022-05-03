from django.shortcuts import render
from django.shortcuts import redirect
from shared.context_init import context_init
from shared.models import Action
from shared.models import Refugee
from shared.models import PhotoTaken

# Create your views here.
def log(request ,rid):

  context = context_init(request)
  if not (context['is_authenticated'] and (context['is_organizer'] or context['is_photographer'])):
    return redirect('/')

  context['rid'] = rid
  refugee = Refugee.objects.filter(rid=rid).first()
  context['found'] = not not refugee

  if context['found'] and context['is_photographer']: 
    action = Action.objects.get(action = 'add')
    photographer = request.user
    record = PhotoTaken(
      action = action
      ,photographer = photographer
      ,refugee = refugee
    )
    record.save()

  return render(request, 'photographer_log.html', context=context)

from django.shortcuts import render
from shared.context_init import context_init
from shared.models import Action
from shared.models import Refugee
from shared.models import PhotoTaken

# Create your views here.
def log(request ,rid):

  context = context_init(request)
  if not (context['is_authenticated'] and (context['is_staff'] or context['is_photographer'])):
    return redirect('/')

  if context['is_photographer']: 
    action = Action.objects.get(action = 'add')
    photographer = request.user
    refugee = Refugee.objects.get(rid=rid)
    record = PhotoTaken(
      action = action
      ,photographer = photographer
      ,refugee = refugee
      )
    record.save()

  context['rid'] = rid
  return render(request, 'photographer_log.html', context=context)

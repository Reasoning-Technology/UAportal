


def context_init(request):
  context = {
    'function':'idle' 
    ,'is_authenticated':request.user.is_authenticated
    ,'is_photographer':False
    ,'is_organizer':False
    }

  if context['is_authenticated']:
    context['is_photographer'] = request.user.groups.filter(name='photographer').exists()
    context['is_organizer'] = request.user.groups.filter(name='organizer').exists()

  return context



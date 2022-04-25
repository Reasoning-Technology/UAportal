


def context_init(request):
  context = {
    'function':'idle' 
    ,'is_authenticated':request.user.is_authenticated
    ,'is_photographer':False
    ,'is_staff':False
    }

  if context['is_authenticated']:
    context['is_photographer'] = request.user.groups.filter(name='photographer').exists()
    context['is_staff'] = request.user.groups.filter(name='staff').exists()

  return context



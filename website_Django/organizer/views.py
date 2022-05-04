from django.shortcuts import render
from django.shortcuts import redirect
#from django.views import generic
from django.urls import reverse
from shared.context_init import context_init
from shared.models import Action
from shared.models import Photographer
from shared.models import Refugee
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.mail import send_mail

# Create your views here.

def photographer(request):

  # must be organizer to use this page!
  context = context_init(request)
  if not context['is_authenticated'] or not context['is_organizer']:
    return redirect('/')

  if request.method == 'POST':
    if 'add' in request.POST:
      context['function'] = 'add'
    elif 'edit' in request.POST:
      context['function'] = 'edit'
    elif 'delete' in request.POST:
      context['function'] = 'delete'
    elif 'submit_add' in request.POST:
      email = request.POST['contact_email']
      record = Photographer(
        shop_name      = request.POST['shop_name']
        ,shop_street   = request.POST['shop_street']
        ,shop_city     = request.POST['shop_city']
        ,shop_country  = request.POST['shop_country']
        ,contact_email = email
        ,contact_phone = request.POST['contact_phone']
        ,contact_name  = request.POST['contact_name']
        )
      record.save()
      user = User.objects.create_user( username=email ,email=email)
      group = Group.objects.get(name='photographer') 
      group.user_set.add(user)
      send_mail(
        'New Photographer Account'
        ,"Please login and hit the 'reset password'  link"
        ,'no-reply@UAportal.org'
        ,[email]
        ,fail_silently=False
      )

  return render(request, 'organizer_photographer.html', context=context)

def refugee(request):
  
  # must be organizer to use this page!
  context = context_init(request)
  if not context['is_authenticated'] or not context['is_organizer']:
    response = redirect('/')
    return response

  if request.method == 'POST':
    if 'add' in request.POST:
      context['function'] = 'add'
    elif 'submit-add' in request.POST:
      record = Refugee(
        email = request.POST['email']
        ,phone = request.POST['phone']
        ,last = request.POST['last']
        ,first_etc = request.POST['first_etc']
        )
      record.save()
      return redirect('refugee_print_QR' ,record.rid)

  return render(request, 'organizer_refugee.html', context=context)


def refugee_print_QR(request ,rid):

  context = context_init(request)
  if not context['is_authenticated'] or not context['is_organizer']:
    return redirect('/')

  context['rid'] = rid
#  context['url'] = '127.0.0.1:8000/photographer/log/' + rid
#   context['url'] = reverse('photographer_log', rid)
  context['url'] = reverse('photographer_log', kwargs={'rid':rid})

  return render(request, 'organizer_refugee_print_QR.html', context=context)







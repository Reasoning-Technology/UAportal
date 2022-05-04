from django.db import models
from . import rand
from django.contrib.auth import get_user_model

AUTH_USER_MODEL = get_user_model()

#--------------------------------------------------------------------------------
class Action(models.Model):
  action = models.CharField(max_length=20)
  def __str__(self):
    return str(self.action)

  # I want to see the table name in places the table name is written, not something else
  class Meta:
    verbose_name = 'Action'
    verbose_name_plural = 'Action'

#--------------------------------------------------------------------------------
class Photographer(models.Model):
  date = models.DateField(auto_now=True);
  action = models.ForeignKey('Action' ,on_delete=models.SET_NULL ,null=True)
  organizer =  models.ForeignKey(AUTH_USER_MODEL ,on_delete=models.SET_NULL ,null=True)
  shop_name =  models.CharField(max_length=40, help_text='shop name')
  shop_street =  models.CharField(max_length=40, help_text='shop street')
  shop_city =  models.CharField(max_length=40, help_text='shop city')
  shop_country =  models.CharField(max_length=40, help_text='shop name')

  contact_email  = models.EmailField(help_text='contact email' ,blank=True)
  contact_phone = models.CharField(max_length=40, help_text='phone number')
  contact_name =  models.CharField(max_length=40, help_text='contact name')

  def __str__(self):
    return self.contact_email

  class Meta:
    ordering = ['date']  
    # I want to see the table name in places the table name is written, not something else
    verbose_name = 'Photographer'
    verbose_name_plural = 'Photographer'

#--------------------------------------------------------------------------------

class Refugee(models.Model):
  date = models.DateField(auto_now=True);
  action = models.ForeignKey('Action' ,on_delete=models.SET_NULL ,null=True)
  organizer =  models.ForeignKey(AUTH_USER_MODEL ,on_delete=models.SET_NULL ,null=True)
  rid = models.CharField(max_length=20)
  email  = models.EmailField(help_text='email' ,blank=True)
  phone = models.CharField(max_length=40, help_text='phone number' ,blank=True)
  last   = models.CharField(max_length=40, help_text='last name' ,blank=True)
  first_etc  = models.TextField(help_text='first name etc.' ,blank=True)

  # def __init__(self):
  #   fields[first].required=False

  def save(self, *args, **kwargs):
    rid = rand.string(8)
    recs = Refugee.objects.filter(rid=rid)
    i = 0
    while len(recs) > 0 and i < 1e3:
      i+=1
      rid = rand.string(8)
      recs = Refugee.objects.filter(rid=rid)
    self.rid = rid
    super(Refugee, self).save(*args, **kwargs)

  def __str__(self):
    return self.rid

  class Meta:
    ordering = ['date']  
    # I want to see the table name in places the table name is written, not something else
    verbose_name = 'Refugee'
    verbose_name_plural = 'Refugee'
    
#--------------------------------------------------------------------------------
# by default a record has a command of 'add'
# a photographer may change the command to 'delete' but the record remains
class PhotoTaken(models.Model):
  date = models.DateTimeField(auto_now=True);
  action = models.ForeignKey('Action' ,on_delete=models.SET_NULL ,null=True)
  photographer =  models.ForeignKey('Photographer' ,on_delete=models.SET_NULL ,null=True)
  refugee = models.ForeignKey('Refugee' ,on_delete=models.SET_NULL ,null=True)
  
  def __str__(self):
    return str(self.date)

  class Meta:
    ordering = ['date']  
    # I want to see the table name in places the table name is written, not something else
    verbose_name = 'PhotoTaken'
    verbose_name_plural = 'PhotoTaken'

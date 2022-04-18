from django.db import models

class EditCommand(models.Model):
  command = models.TextField()
  def __str__(self):
    return str(self.command)

# Create your models here.
class Photographer(models.Model):
  date = models.DateField(auto_now=True);
  action = models.ForeignKey('EditCommand' ,on_delete=models.SET_NULL ,null=True)
  name = models.CharField(max_length=200, help_text='enter the name of the photographer')

  class Meta:
    ordering = ['name']  

  def __str__(self):
    return self.name

#placeholder
import random
def gen_number():
  return random.randrange(10**12 ,10**13-1)

class Refugee(models.Model):
  date = models.DateField(auto_now=True);
  action = models.ForeignKey('EditCommand' ,on_delete=models.SET_NULL ,null=True)
  number = models.PositiveIntegerField()
  last   = models.TextField(help_text='nom' ,blank=True)
  first_etc  = models.TextField(help_text='prénom' ,blank=True)
  email  = models.EmailField(help_text='email' ,blank=True)

  # def __init__(self):
  #   fields[first].required=False

  class Meta:
    ordering = ['number']  

  def save(self, *args, **kwargs):
    self.number = gen_number()
    super(Refugee, self).save(*args, **kwargs)

  def __str__(self):
    return str(self.number)

# by default a record has a command of 'add'
# a photographer may change the command to 'delete' but the record remains
class PhotoTaken(models.Model):
  date = models.DateTimeField(auto_now=True);
  action = models.ForeignKey('EditCommand' ,on_delete=models.SET_NULL ,null=True)
  photographer = models.ForeignKey('Photographer' ,on_delete=models.SET_NULL ,null=True)
  refugee = models.ForeignKey('Refugee' ,on_delete=models.SET_NULL ,null=True)
  
  class Meta:
    ordering = ['refugee']  

  def __str__(self):
    return str(self.date)


from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.

from .models import Photographer ,Refugee ,EditCommand ,PhotoTaken
admin.site.register(EditCommand)


# looks like a better way:
# class MyModelAdmin(ModelAdmin):
#     class Media:
#         css = {"all": ("my_stylesheet.css",)}
# .column-foo {
#     width: 20px;
# }
# where "foo" is a field name.

# Source: https://docs.djangoproject.com/en/3.0/topics/forms/media/


class LocalModelAdmin(admin.ModelAdmin):
  formfield_overrides = {
    models.TextField: {'widget': TextInput(attrs={'size':'60'})}
    #,models.BigIntegerField(default=1, validators=[MinValueValidator(10**12), MaxValueValidator(10**14),], )
    #    ,models.CharField: {'widget': TextInput(attrs={'size':'20'})}
    #    ,models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':20})}
  }

class PhotographerTable(LocalModelAdmin):
    list_display = ('date' ,'action' ,'name')
    list_filter = ('date' ,'action' ,'name')
admin.site.register(Photographer, PhotographerTable)

class RefugeeTable(LocalModelAdmin):
    list_display = ('date' ,'action' ,'number' ,'last' ,'first_etc' ,'email')
    list_filter = ('date' ,'action' ,'number' ,'last' ,'first_etc' ,'email')
admin.site.register(Refugee, RefugeeTable)

class PhotoTakenTable(LocalModelAdmin):
    list_display = ('date' ,'action' ,'refugee' ,'photographer' )
    list_filter = ('date' ,'action' ,'refugee' ,'photographer' )
admin.site.register(PhotoTaken, PhotoTakenTable)


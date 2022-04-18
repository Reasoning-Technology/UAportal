# Data Migraion 2022-04-06 16:24

from django.db import migrations

def EditCommand_init(apps ,schema_editor):
  EditCommand = apps.get_model('photo_accounting' ,'EditCommand')
  EditCommand(command='add').save()
  EditCommand(command='delete').save()

class Migration(migrations.Migration):

    dependencies = [
      ('photo_accounting', '0002_auto_20220406_1615'),
    ]

    operations = [
      migrations.RunPython(EditCommand_init)
    ]

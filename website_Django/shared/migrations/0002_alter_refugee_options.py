# Generated by Django 3.2.13 on 2022-04-25 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refugee',
            options={'ordering': ['date'], 'verbose_name': 'Refugee', 'verbose_name_plural': 'Refugee'},
        ),
    ]

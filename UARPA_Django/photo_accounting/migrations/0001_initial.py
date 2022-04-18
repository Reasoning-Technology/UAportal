# Generated by Django 3.2.12 on 2022-04-05 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.CharField(help_text='enter the name of the photographer', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Refugee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('first', models.CharField(blank=True, help_text='prénom', max_length=120)),
                ('second', models.CharField(blank=True, help_text='optional autre nom', max_length=120)),
                ('last', models.CharField(blank=True, help_text='nom', max_length=120)),
                ('email', models.EmailField(blank=True, help_text='email', max_length=254)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='PhotoTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('photographer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo_accounting.photographer')),
                ('refugee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo_accounting.refugee')),
            ],
            options={
                'ordering': ['refugee'],
            },
        ),
    ]

# Generated by Django 4.0 on 2021-12-14 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmacia',
            old_name='functionamiento_dia',
            new_name='funcionamiento_dia',
        ),
    ]
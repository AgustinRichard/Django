# Generated by Django 3.2.13 on 2022-04-24 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mascotas', '0003_alter_mascota_observaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='dueno',
            new_name='dueño',
        ),
        migrations.RenameField(
            model_name='mascota',
            old_name='fecha_nacimiento',
            new_name='fecha_de_nacimiento',
        ),
    ]

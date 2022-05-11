# Generated by Django 3.2.13 on 2022-05-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('descripcion', models.CharField(max_length=60)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(choices=[('hardware', 'Hardware'), ('software', 'Software'), ('insumos', 'Insumos'), ('servicios', 'Servicios'), ('varios', 'Varios')], default='hardware', max_length=10)),
            ],
        ),
    ]

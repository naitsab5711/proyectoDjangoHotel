# Generated by Django 3.2.5 on 2021-07-05 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veranumApp', '0002_user_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('tipo_Habitacion', models.IntegerField()),
                ('cantidad_camas', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('piso', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
    ]

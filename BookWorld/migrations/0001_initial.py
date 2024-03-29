# Generated by Django 4.1.2 on 2023-02-15 12:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='DNI')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Fecha Alta')),
                ('address', models.CharField(max_length=150, null=True, verbose_name='Dirección')),
                ('phone', models.CharField(max_length=150, null=True, verbose_name='Nº telefono')),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('genre', models.CharField(max_length=150, null=True)),
                ('price', models.FloatField(max_length=150, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookWorld.author')),
            ],
        ),
    ]

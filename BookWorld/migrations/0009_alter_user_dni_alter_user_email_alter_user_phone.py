# Generated by Django 4.0.8 on 2023-02-26 17:34

import BookWorld.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookWorld', '0008_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, validators=[BookWorld.models.user.validateDni], verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150, validators=[BookWorld.models.user.validateEmail], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=9, null=True, verbose_name='Nº telefono'),
        ),
    ]
# Generated by Django 4.0.8 on 2023-02-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookWorld', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, unique=True),
        ),
    ]

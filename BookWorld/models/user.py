from django.db import models
from datetime import datetime

class User(models.Model):
    dni = models.CharField('DNI',max_length=10, primary_key=True)
    name = models.CharField('Nombre',max_length=150, blank=False, null=False)
    email = models.EmailField('Email',max_length=150, blank=False, null=False)
    date = models.DateField('Fecha Alta', blank=False, null=False,default=datetime.now)
    address = models.CharField('Dirección',max_length=150, blank=False, null=True)
    phone = models.CharField('Nº telefono',max_length=150, blank=False, null=True)
    admin = models.BooleanField(default=False)

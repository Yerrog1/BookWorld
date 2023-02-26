from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
from datetime import datetime


def validateDni(value):
    table = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(value) == 9:
        leter = value[8].upper()
        numbers = value[:8]
        calc = int(numbers) % 23
        if table[calc] == leter:
            return True
    return False
def validateEmail(value):
    try:
        validate_email(value)
        return True
    except ValidationError:
        return False


class User(models.Model):
    dni = models.CharField('DNI', max_length=9, primary_key=True, validators=[validateDni], blank=False, null=False)
    name = models.CharField('Nombre', max_length=150, blank=False, null=False)
    email = models.EmailField('Email', max_length=150, blank=False, null=False,validators=[validateEmail])
    date = models.DateField('Fecha Alta', blank=False, null=False, default=datetime.now)
    address = models.CharField('Dirección', max_length=150, blank=False, null=True)
    phone = models.CharField('Nº telefono', max_length=9, blank=False, null=True)
    admin = models.BooleanField(default=False)

    def clean(self):
        super(User, self).clean()
        if not validateDni(self.dni):
            raise ValidationError("El DNI introducido no es válido")
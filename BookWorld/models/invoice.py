from django.db import models

class Invoice(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)






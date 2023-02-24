from django.db import models


class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)

    isbn = models.ForeignKey('Book', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)


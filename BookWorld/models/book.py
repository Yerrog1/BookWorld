from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True, blank=False, null=False, unique=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=2000, blank=False, null=False)
    author = models.ForeignKey("Author", null=False, on_delete=models.CASCADE)
    genre = models.CharField(max_length=150, blank=False, null=True)
    price = models.FloatField(max_length=150, blank=False, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)





from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=50,blank=False,null=False)

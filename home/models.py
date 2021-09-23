from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.FloatField()

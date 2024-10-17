from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)

class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='streets', on_delete=models.CASCADE)

class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

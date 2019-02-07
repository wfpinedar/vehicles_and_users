from django.db import models
from . import data

# Create your models here.
"""In this section """
class Owner(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_image = models.FileField(upload_to='owners/ids/')
    id = models.PositiveIntegerField(primary_key=True)
    def __str__(self):
        return f"{self.name} {self.last_name} - {self.id}"

class Vehicle(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    trademark = models.IntegerField(choices=data.TRADEMARK_CHOICES)
    type = models.CharField(max_length=20)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} {self.owner.name} {self.owner.name}"

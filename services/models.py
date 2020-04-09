from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    place = models.CharField(max_length=200)
    modality = models.CharField(max_length=100)

    def __str__(self):
        return self.name
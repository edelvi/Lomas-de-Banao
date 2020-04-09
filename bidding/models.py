from django.db import models
from services.models import Services

# Create your models here.
class Bidding(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    duration = models.IntegerField(max_length=20)
    services = models.ManyToManyField(Services, related_name="services")

    def __str__(self):
        return self.name
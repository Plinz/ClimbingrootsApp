from django.db import models
from crags.enums import RouteType, Grade


class Crag(models.Model):

    name = models.CharField(max_length=500)
    lon = models.FloatField
    lat = models.FloatField
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Route(models.Model):
    crag = models.ForeignKey(Crag, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=255, choices=RouteType.choices())
    openIn = models.DateField()
    faIn = models.DateField()
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
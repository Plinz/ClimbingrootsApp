from django.db import models
from crags.enums import RouteType, Grade
from django_countries.fields import CountryField


class Crag(models.Model):
    country = CountryField()
    name = models.CharField(max_length=500)
    lon = models.FloatField
    lat = models.FloatField
    address = models.CharField(max_length=500)
    isValidated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Route(models.Model):
    crag = models.ForeignKey(Crag, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=255, choices=RouteType.choices())
    openIn = models.DateField()
    faIn = models.DateField()
    description = models.CharField(max_length=5000)
    isValidated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Anecdote(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    anecdote = models.TextField()
    source = models.CharField(max_length=500)
    isValidated = models.BooleanField(default=False)

    def __str__(self):
        return self.route.name


class NameStory(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    story = models.TextField()
    source = models.CharField(max_length=500)
    isValidated = models.BooleanField(default=False)

    def __str__(self):
        return self.route.name

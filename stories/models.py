from django.db import models


class Anecdote(models.Model):
    route = models.ForeignKey('crags.Route', on_delete=models.CASCADE)
    anecdote = models.CharField(max_length=5000)
    source = models.CharField(max_length=500)
    isValidated = models.BooleanField(default=False)

    def __str__(self):
        return self.route.name


class NameStory(models.Model):
    route = models.ForeignKey('crags.Route', on_delete=models.CASCADE)
    story = models.CharField(max_length=5000)
    source = models.CharField(max_length=500)
    isValidated = models.BooleanField(default=False)

    def __str__(self):
        return self.route.name

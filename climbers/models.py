from django.db import models


class Climber(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    birthDate = models.DateField()

    def __str__(self):
        return self.firstName + self.lastName

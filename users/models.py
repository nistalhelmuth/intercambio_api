from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    img = models.URLField(max_length=500, blank=True, null = True)

    def __str__(self):
        return self.username + ' (' + str(self.id) + ')'

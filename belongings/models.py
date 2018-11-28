from django.db import models
from categories.models import Category
from users.models import User


class Belonging(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    STATE_CHOICES = [(0, 'very bad'), (1, 'bad'),(2, 'good'), (3, 'very good'), (4, 'excelent')]
    state = models.IntegerField(choices=STATE_CHOICES, default='good')
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True)
    img = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

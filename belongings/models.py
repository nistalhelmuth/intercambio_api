from django.db import models
from categories.models import Category
from users.models import User


class Belonging(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    STATE_CHOICES = [('awful', 'awful'), ('very bad', 'very bad'), ('bad', 'bad'),
                     ('regular', 'regular'), ('good', 'good'), ('very good', 'very good'), ('excelent', 'excelent')]
    state = models.CharField(
        max_length=10, choices=STATE_CHOICES, default='good')
    belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True)

from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=100)


class User(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)


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


class Post(models.Model):
    description = models.CharField(max_length=4000)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    offered_item = models.ForeignKey(
        Belonging, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)


class Offer(models.Model):
    offered_object = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    offered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    offered_in = models.ForeignKey(Post, on_delete=models.CASCADE)

from django.db import models
from belongings.models import Belonging
from categories.models import Category
from users.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    offered_item = models.ForeignKey(
        Belonging, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title + ' (' + str(self.id) + ')'

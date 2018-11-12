from django.db import models
from belongings.models import Belonging
from users.models import User
from posts.models import Post

class Offer(models.Model):
    offered_object = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    offered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    offered_in = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.offered_in + ' (' + str(self.id) + ')'

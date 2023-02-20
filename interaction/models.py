from django.db import models
from django.contrib.auth.models import User
from gallery.models import Flower

# Create your models here.
class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='actions')
    liked = models.BooleanField(null=True)

    class Meta:
        unique_together = ['user', 'flower']

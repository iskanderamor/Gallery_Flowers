from django.db import models

# Create your models here.

class Flower(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    description = models.TextField()
    description_ar = models.TextField()

    def __str__(self) -> str:
        return self.title

from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    price = models.CharField(max_length=255, null=False)
    dateAdded = models.DateTimeField(default=timezone.now)
    URL = models.CharField(max_length=1000, null=False)
    image = models.CharField(max_length=1000, null=False)
    title = models.CharField(max_length=1000, null=False)

    def __str__(self):
            return self.image

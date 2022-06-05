from django.db import models

# Create your models here.
import uuid

uuid.uuid4().hex[:6].upper()

class Book(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True, editable=False)
    title  = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
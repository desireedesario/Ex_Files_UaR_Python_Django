from django.db import models

# Create your models here.
#The models.py file contains the set of models for the Django app.
#A model is a class inheriting from django.db.models.Model, and is used to define fields as class attributes.
class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

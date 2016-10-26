from django.db import models

# Create your models here.
#The models.py file contains the set of models for the Django app.
#A model is a class inheriting from django.db.models.Model, and is used to define fields as class attributes.

#different type of fields you may use
    #Numbers
        #IntegerField - 1, -1, 3, 0
        #DecimalField - 0.5, 2.4, 3.7
    #text fields
        #Charfield - "Product Name"
        #TextField - "To elaborate on my point..."
        #EmailField - desi@gmail.com
        #URLField - www.desi.com
    #File fields
        #FileField - user_uploaded.docx
        #ImageField - best_avatar.jpg
    #Boolean fields
        #BooleanField - obviously true or false
        #DateTimeField - datetime(1969, 1, 1, 8, 0, 0)

    #different types of field attributes
        #max-length : used to define the maximum length of a CharField or one of its child fields.
        #null : no data
        #blank : empty string
        #default : set a default value to a field.
        #choices : can limit the value that is stored into this field. 
class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

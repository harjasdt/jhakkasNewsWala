from django.db import models

# Create your models here.
from pyexpat import model
from django.db import models

class QUESTION(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
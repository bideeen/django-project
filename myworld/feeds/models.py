from django.db import models

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=40)
    post = models.CharField(max_length=1000)
    time = models.CharField(max_length=500)
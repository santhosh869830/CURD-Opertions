from django.db import models
from django.urls import reverse
# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=15)
    nbr=models.IntegerField()
    add=models.TextField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detailC',kwargs={'pk':self.pk})



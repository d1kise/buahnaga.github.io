from django.db import models

# Create your models here.

class TableCars(models.Model):  
    eid = models.CharField(max_length=20)  
    ebrand = models.CharField(max_length=100)  
    emodel = models.CharField(max_length=100)
    eprice = models.IntegerField()
    class Meta: 
        db_table = "Cars"
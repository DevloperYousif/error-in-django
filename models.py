
from django.db import models

class Female(models.Model):
    name_female = models.CharField(max_length=50 ,null=True)
    def __str__(self):
        return self.name_female
class Male(models.Model):
    name_male = models.CharField(max_length=50, null=True)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_female
    
class Product(models.Model):
    title = models.CharField(max_length=50,null=True) 
    def __str__(self):
        return self.title 
    
    
class User(models.model):
    name = models.CharField(max_length=50,null=True)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Video (models.Model):
    title = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.title
    
class User (models.Model):
    title = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.title

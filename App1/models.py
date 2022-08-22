from django.db import models

# Create your models here.

class Sick (models.Model):
    sickId = models.AutoField(primary_key=True)
    sickName=models.CharField(max_length=100)
    sickEmail=models.EmailField()

class Docktur (models.Model):
    DocId=models.AutoField(primary_key=True)
    DocName=models.CharField(max_length=100) 
    Docspecialty=models.CharField(max_length=100)
    docEmail=models.EmailField()

class Diseases(models.Model):
    DisId=models.AutoField(primary_key=True)
    DisName=models.CharField(max_length=100)
    DisDescribe=models.CharField(max_length=500)
    specialty=models.CharField(max_length=100)
    
class Recommender(models.Model):
    DisId = models.AutoField(primary_key=True)
    DisName=models.CharField(max_length=100)
    Recomend=models.CharField(max_length=100)


    
from django.db import models
from datetime import datetime


# Create your models here.
class Tagmodel(models.Model):

    name = models.CharField(max_length=50)
    uom = models.CharField(max_length=30)
    description = models.CharField(max_length=124)
    measured_property = models.CharField(max_length = 50, blank=True, null=True)
    csv_filename = models.CharField(max_length=124)
    time_points = models.IntegerField(blank=True, null=True)
    data_points = models.IntegerField(blank=True, null=True)
    average = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name 

class Datafile(models.Model):
    description = models.CharField(max_length=124, blank=True, null=True)
    csvfile = models.FileField(upload_to='csvfiles/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.csvfile.name 

class Batch(models.Model):
    datafile = models.ForeignKey('Datafile', on_delete=models.CASCADE, blank=True, null=True)
    dayfirst = models.BooleanField(default=True)
    skiprows = models.IntegerField(default=0)
    tagsIdentified = models.IntegerField(blank=True, null=True)
    # tagsSaved = models.IntegerField(blank=True, null=True)
    # status = models.CharField(max_length=124, blank=True, null=True)

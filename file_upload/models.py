from django.db import models

# Create your models here.
class Tagmodel(models.Model):

    name = models.CharField(max_length=50, unique=True)
    uom = models.CharField(max_length=30)
    description = models.CharField(max_length=124)
    measured_property = models.CharField(max_length = 50, blank=True, null=True)
    csv_filename = models.CharField(max_length=124)
    time_points = models.IntegerField(blank=True, null=True)
    data_points = models.IntegerField(blank=True, null=True)
    average = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    # @property
    # def perc_complete(self):
    #     if self.data_points>0:
    #         return self.data_points/self.time_points

    #     return 0

    def __str__(self):
        return self.name 

class Datafile(models.Model):
    description = models.CharField(max_length=124, blank=True, null=True)
    csvfile = models.FileField(upload_to='csvfiles/')
    status = models.CharField(max_length=124, blank=True, null=True)

    def __str__(self):
        return self.csvfile.name 

from django.db import models


# Create your models here.
class MeterReading(models.Model):
    flow_reference = models.CharField(max_length=30)
    flow_name = models.CharField(max_length=30)



class Album(models.Model):
    meter_reading = models.ForeignKey(MeterReading, on_delete=models.CASCADE)
    mpan = models.CharField(max_length=100)
    meter_serial_number = models.CharField(max_length=100)
    date = models.DateField()
    reading = models.IntegerField()
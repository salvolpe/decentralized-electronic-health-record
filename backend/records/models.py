from django.contrib.gis.db import models

class ConfirmedCase(models.Model):
    location = models.PointField()
    estimated_date_contracted = models.DateTimeField('estimated date contracted')
    date_confirmed = models.DateTimeField('date confirmed')

class ContagionSite(models.Model):
    confirmed_case = models.ForeignKey(ConfirmedCase, on_delete=models.CASCADE)
    transmission_site = models.PointField()
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')

from django.db import models
from sweethandy.users.models import User
# Register your models here.


class Meal(models.Model):
    timeofmeal = models.DateTimeField(null=True, blank=True)
    contents = models.CharField(max_length=200, null=True, blank=True)
    imagelink = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Measurement(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    timeofmeasurement = models.DateTimeField(null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)

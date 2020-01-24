from rest_framework import serializers
from .models import Meal, Measurement

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'timeofmeal', 'user', 'contents', 'imagelink', )

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('id', 'meal', 'timeofmeasurement', 'value', )

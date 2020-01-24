from rest_framework import viewsets
from .models import Meal, Measurement
from .serializers import MealSerializer, MeasurementSerializer

class MealViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves meals
    """
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves measurements
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

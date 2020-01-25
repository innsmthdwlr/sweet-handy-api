from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Meal, Measurement
from .serializers import MealSerializer, MeasurementSerializer

class MealViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves meals
    """
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves measurements
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

from django.contrib import admin
from .models import Meal, Measurement


class MeasurementInLine(admin.TabularInline):
    model = Measurement
    extra = 1

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    fields = ['timeofmeal', 'contents', 'imagelink', 'user']

    inlines = [MeasurementInLine]
    list_display = ('id', 'user', 'timeofmeal', )
    list_filter = ['user']
    search_fields = ['contents']

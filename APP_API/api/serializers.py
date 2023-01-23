from rest_framework import serializers
from .models import TableCars

class TableCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableCars
        fields = "__all__"
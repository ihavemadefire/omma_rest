from rest_framework import serializers
from .models import Dispensary


class DispensarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispensary
        fields = '__all__'
from rest_framework import serializers
from .models import WasteBank, WasteType, OpeningHour

class WasteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteType
        fields = ['id', 'name']

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = ['day', 'open_time', 'close_time']

class WasteBankSerializer(serializers.ModelSerializer):
    waste_processed = WasteTypeSerializer(many=True, read_only=True)
    opening_hours = OpeningHourSerializer(many=True, read_only=True)

    class Meta:
        model = WasteBank
        fields = [
            'id', 'name', 'latitude', 'longitude',
            'waste_processed',
            'opening_hours',
        ]
\

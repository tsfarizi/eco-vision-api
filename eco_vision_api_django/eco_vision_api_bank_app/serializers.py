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

class WasteBankCreateSerializer(serializers.ModelSerializer):
    waste_processed = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True
    )
    opening_hours = OpeningHourSerializer(many=True, write_only=True)

    class Meta:
        model = WasteBank
        fields = ['id', 'name', 'latitude', 'longitude', 'waste_processed', 'opening_hours']

    def create(self, validated_data):
        waste_ids = validated_data.pop('waste_processed')
        opening_hours_data = validated_data.pop('opening_hours')
        bank = WasteBank.objects.create(**validated_data)
        bank.waste_processed.set(WasteType.objects.filter(id__in=waste_ids))

        for oh in opening_hours_data:
            OpeningHour.objects.create(bank=bank, **oh)

        return bank

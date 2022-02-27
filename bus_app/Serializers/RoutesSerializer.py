from bus_app.Serializers.LocationSerializer import LocationSerializer
from rest_framework import serializers
from ..models import Routes, Location


class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'

    def create(self, validated_data):
        try:
            locationFrom = Location.objects.get(pk=validated_data.get('locationFrom', None))
            locationTo = Location.objects.get(pk=validated_data.get('locationTo', None))
            if locationTo is not None and locationFrom is not None:
                instance = Routes()
                instance.locationTo = locationTo
                instance.locationFrom = locationFrom
                instance.save()
                return instance
            return AttributeError("'Expected 'locationFrom' and 'locationTo'")
        except Exception as e:
            return AttributeError(e)
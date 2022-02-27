from rest_framework import serializers
from bus_app.Serializers.LocationSerializer import LocationSerializer
from bus_app.Serializers.RoutesSerializer import RoutesSerializer
from bus_app.Serializers.VehicleSeriaizer import VehicleSeriaizer
from ..models import StopsOnRoutes, Vehicle, Routes, Location


class StopsSerializer(serializers.ModelSerializer):
    vehicle = VehicleSeriaizer(read_only=True)
    route = RoutesSerializer(read_only=True)
    stopLocation = LocationSerializer(read_only=True)
    class Meta:
        model = StopsOnRoutes
        fields = ('vehicle','route','stopLocation', 'stopPriority', 'fare',)

    def createStop(self, validated_data):
        vehicle = Vehicle.objects.filter(regNumber = validated_data.get('vehicle', None)).first()
        route = Routes.objects.get(pk = validated_data.get('route', None))
        stopLocation = Location.objects.get(pk = validated_data.get('stopLocation', None))
        if vehicle is not None and route is not None and stopLocation is not None and validated_data.get('stopPriority', None) is not None:
            instance = StopsOnRoutes(stopLocation = stopLocation)
            instance.route = route
            instance.vehicle = vehicle
            instance.stopPriority = validated_data.get('stopPriority', None)
            instance.fare = validated_data.get('fare', None)
            instance.save()
            return instance
        return AttributeError("Expected 'vehicle','route','stopLocation', 'stopPriority', 'fare'")


    def updateStop(self, validated_data, user):
        if validated_data.get('id', None) is not None:
            stop = StopsOnRoutes.objects.get(pk
                = validated_data.get('id', None))
            stop.stopLocation = Location.objects.get(pk = validated_data.get('stopLocation', stop.stopLocation))
            stop.stopPriority = validated_data.get('stopPriority', stop.stopPriority)
            stop.fare = validated_data.get('fare', stop.fare)
            stop.save()
            return stop
        return AttributeError("'id' is missing")
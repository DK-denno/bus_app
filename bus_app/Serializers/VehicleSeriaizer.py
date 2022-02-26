from rest_framework import serializers
from ..models import Vehicle


class VehicleSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        exclude = ('driver',)


    def createVehicle(self, validated_data, request):
        regNumber = validated_data.get('regNumber', None)
        numberOfSeats = validated_data.get('numberOfSeats', None)
        if regNumber is not None and numberOfSeats is not None:
            print("---------------------->" + request.user.username)
            instance = Vehicle(
                regNumber = regNumber, numberOfSeats = numberOfSeats)
            instance.driver = request.user
            instance.save()
            return instance
        raise AttributeError("Either 'name','regNumber' or 'numberOfSeats' is missing")

    def updateVehicle(self, validated_data, user):
        if validated_data.get('vehicle_id', None) is not None:
            vehicle = Vehicle.objects.get(pk
                = validated_data.get('vehicle_id', None),
                driver = user)
            vehicle.regNumber = validated_data.get('regNumber', vehicle.regNumber)
            vehicle.numberOfSeats = validated_data.get('numberOfSeats', vehicle.numberOfSeats)
            vehicle.driver = user
            vehicle.save()
            return vehicle
        raise AttributeError("'vehicle_id' is missing")
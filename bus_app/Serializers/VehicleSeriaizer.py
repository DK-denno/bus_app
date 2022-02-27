from bus_app.Serializers.UserSerializer import UserSerializer
from rest_framework import serializers
from ..models import Vehicle


class VehicleSeriaizer(serializers.ModelSerializer):
    driver = UserSerializer(read_only=True)
    class Meta:
        model = Vehicle
        fields = '__all__'

    def createVehicle(self, validated_data, request):
        regNumber = validated_data.get('regNumber', None)
        numberOfSeats = validated_data.get('numberOfSeats', None)
        if regNumber is not None and numberOfSeats is not None:
            if numberOfSeats >= 14 and numberOfSeats <= 67:
                instance = Vehicle(
                    regNumber = regNumber, numberOfSeats = numberOfSeats)
                instance.driver = request.user
                instance.save()
                return instance
            raise AttributeError("Seats should be between 14 and 67")
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
        return AttributeError("'vehicle_id' is missing")
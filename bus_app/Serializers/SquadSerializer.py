from multiprocessing.spawn import import_main_path
from operator import imod
from bus_app.Serializers.LocationSerializer import LocationSerializer
from bus_app.Serializers.RoutesSerializer import RoutesSerializer
from bus_app.Serializers.VehicleSeriaizer import VehicleSeriaizer
from rest_framework import serializers
from ..models import Squad, Vehicle, Routes
from datetime import datetime


class SquadSerializer(serializers.ModelSerializer):
    vehicle = VehicleSeriaizer(read_only=True)
    route = RoutesSerializer(read_only=True)
    class Meta:
        model = Squad
        fields = '__all__'

    def createSquad(self, validated_data):
        vehicle = Vehicle.objects.filter(regNumber = validated_data.get('vehicle', None)).first()
        route = Routes.objects.get(pk = validated_data.get('route', None))
        depatureTime = datetime.fromtimestamp(validated_data.pop('depatureTime', None))
        arrivalTime = datetime.fromtimestamp(validated_data.pop('arrivalTime', None))
        priority = validated_data.get('priority', None)
        if vehicle is not None and route is not None and depatureTime is not None and arrivalTime is not None:
            instance = Squad(depatureTime=depatureTime, arrivalTime=arrivalTime)
            instance.route = route
            instance.regNumber = vehicle.regNumber
            instance.vehicle = vehicle
            instance.priority = priority
            instance.save()
            return instance
        return AttributeError("Expected 'vehicle','route','depatureTime','arrivalTime'")

    def updateSquad(self, validated_data):
        if validated_data.get('id', None) is not None:
            squad = Squad.objects.get(pk
                = validated_data.get('id', None))
            squad.depatureTime = datetime.fromtimestamp(validated_data.get('depatureTime', datetime.timestamp(squad.depatureTime)))
            squad.arrivalTime = datetime.fromtimestamp(validated_data.get('arrivalTime', datetime.timestamp(squad.arrivalTime)))
            squad.route = Routes.objects.get(pk=validated_data.get('route', squad.route.id))
            squad.vehicle = Vehicle.objects.get(regNumber=validated_data.get('regNumber', squad.vehicle.id))
            squad.priority = validated_data.get('priority', squad.priority)
            squad.save()
            return squad
        return AttributeError("'id' is missing")
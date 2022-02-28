from bus_app.Serializers.UserSerializer import UserSerializer
from rest_framework import serializers
from bus_app.Serializers.LocationSerializer import LocationSerializer
from bus_app.Serializers.SquadSerializer import SquadSerializer
from ..models import Booking, Location, Squad, StopsOnRoutes, Vehicle, Routes
from datetime import datetime
import json


class BookingSerializer(serializers.ModelSerializer):
    passenger = UserSerializer(read_only=True)
    squad = SquadSerializer(read_only=True)
    stopLocation = LocationSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ('squad','passenger','stopLocation', 'seatNumber')

    ## Gets a seat in the new vehicle.
    def bump_seats(self, squad):
        ## Move to next vehicle
        try:
            new_squad = Squad.objects.get(priority = squad.priority + 1)
            return new_squad
        except Exception as e:
            raise Exception(e)


    def getBooking(self, validated_data):
        squad = Squad.objects.get(pk = validated_data.get('squad', None))
        if squad.seatsBooked < squad.vehicle.numberOfSeats:
            return squad
        else:
            return self.bump_seats(squad)

    def veriyStops(self, location, route):
        l = None
        stops = StopsOnRoutes.objects.filter(route = route)
        if stops is not None:
            for stop in stops:
                if stop.stopLocation.name == location.name or stop.stopLocation.name == route.locationFrom.name or stop.stopLocation.name == route.locationTo.name:
                    l = location
            if location.name == route.locationFrom.name and location.name == route.locationTo.name:
                l = location
        return l

    def getEmptySeat(self, validated_data, squad):
        seatNumber = validated_data.get('seatNumber', None)
        try:
            booking = Booking.objects.filter(
                seatNumber = seatNumber, squad = squad).first()
            if booking is not None and seatNumber <= squad.vehicle.numberOfSeats:
                return  squad.seatsBooked + 1
            return seatNumber
        except Exception as e:
            print(e)
            if seatNumber <= squad.vehicle.numberOfSeats:
                return  validated_data.get('seatNumber', None)
        return squad.seatsBooked + 1

    def createBooking(self, validated_data, user):
        if user is not None:
            squad = self.getBooking(validated_data=validated_data)
            stopLocation = self.veriyStops(Location.objects.get(pk
                = validated_data.get('stopLocation', None)), squad.route)
            if stopLocation is not None:
                booking = Booking(
                    passenger = user,
                    squad = squad,
                    stopLocation = stopLocation,
                    seatNumber = self.getEmptySeat(validated_data, squad)
                )
                booking.save()
                squad.seatsBooked = squad.seatsBooked + 1
                squad.save()
                return booking
            return AttributeError("Invalid stop")
        return AttributeError("Expected 'squad','stopLocation'")
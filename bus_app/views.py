from email import message
from lib2to3.pgen2 import driver
from math import prod
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .Serializers import BookingSerializer
from .Serializers import UserSerializer
from .Serializers import RoleSerializer
from .Serializers import ProfileSerializer
from .Serializers import VehicleSeriaizer
from .Serializers import LocationSerializer
from .Serializers import RoutesSerializer
from .Serializers import StopsSerializer
from .Serializers import SquadSerializer
from rest_framework.decorators import api_view, permission_classes
from .models import Booking, Profile, Squad, Vehicle, Role, Location, Routes, StopsOnRoutes
from datetime import datetime

# Create your views here.
def home(request):
    permission_classes = (IsAuthenticated,)
    return render(request, "index.html", {})


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        print(request.user.username)
        return Response(content)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer.UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_role(request):
    serializer = RoleSerializer.RoleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_roles(request):
    roles = Role.objects.all()
    serializer = RoleSerializer.RoleSerializer(roles, many=True)
    return Response(
        {'data': serializer.data},
        status=status.HTTP_201_CREATED
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer.ProfileSerializer(profile)
    return Response({'data': serializer.data},
        status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_profile(self, request):
#     serializer = ProfileSerializer.ProfileSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {'data': serializer.data},
#             status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {'data': serializer.errors},
#         status=status.HTTP_400_BAD_REQUEST
#     )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vehicle(request):
    serializer = VehicleSeriaizer.VehicleSeriaizer(data = request.data)
    serializer.createVehicle(validated_data=request.data, request=request)
    if serializer.is_valid():
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_vehicle(request):
    serializer = VehicleSeriaizer.VehicleSeriaizer(data = request.data)
    serializer.updateVehicle(validated_data=request.data, user=request.user)
    if serializer.is_valid():
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_vehicle(request):
    try:
        vehicle = Vehicle.objects.get(driver=request.user, pk = request.data.get('vehicle_id', None)).delete()
        return Response(
            {'data': {"message":"success"}},
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {'data': {"message":str(e)}},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_Location(request):
    serializer = LocationSerializer.LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_locations(request):
    roles = Location.objects.all()
    serializer = LocationSerializer.LocationSerialize(roles, many=True)
    return Response(
        {'data': serializer.data},
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_Routes(request):
    serializer = RoutesSerializer.RoutesSerializer(data=request.data)
    serializer.create(validated_data=request.data)
    if serializer.is_valid():
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_Routes(request):
    routes = Routes.objects.all()
    serializer = RoutesSerializer.RoutesSerializer(routes, many=True)
    return Response(
        {'data': serializer.data},
        status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_Stops(request):
    serializer = StopsSerializer.StopsSerializer(data=request.data)
    stop = serializer.createStop(validated_data=request.data)
    if serializer.is_valid():
        return Response(
            {'data': StopsSerializer.StopsSerializer(stop).data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_Stops(request):
    stops = StopsOnRoutes.objects.all()
    serializer = StopsSerializer.StopsSerializer(stops, many=True)
    return Response(
        {'data': serializer.data},
        status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_Squad(request):
    serializer = SquadSerializer.SquadSerializer(data=request.data)
    squad = serializer.createSquad(validated_data=request.data)
    if serializer.is_valid():
        return Response(
            {'data': SquadSerializer.SquadSerializer(squad).data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_Squads(request):
    try:
        if(request.data.get("regNumber", None) is not None):
            squads = Squad.objects.filter(regNumber = request.data.get("regNumber", None))
            serializer = SquadSerializer.SquadSerializer(squads, many=True)
        elif(request.data.get("startDate", None) is not None and request.data.get("endDate", None) is not None):
            startDate = datetime.fromtimestamp(request.data.get("startDate", None))
            endDate = datetime.fromtimestamp(request.data.get("endDate", None))
            squads = Squad.objects.filter(depatureTime__range=[startDate, endDate])
            serializer = SquadSerializer.SquadSerializer(squads, many=True)
        else:
            squads = Squad.objects.all()
            serializer = SquadSerializer.SquadSerializer(squads, many=True)
        try:
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {'data': e},
            status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_squad(request):
    serializer = SquadSerializer.SquadSerializer(data=request.data)
    serializer.updateSquad(validated_data=request.data)
    if serializer.is_valid():
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_bookings(request):
    serializer = BookingSerializer.BookingSerializer(data=request.data)
    serializer.createBooking(validated_data=request.data, user=request.user)
    if serializer.is_valid():
         return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_Bookings(request):
    bookings = Booking.objects.filter(passenger = request.user)
    print(bookings)
    serializer = BookingSerializer.BookingSerializer(bookings, many=True)
    return Response(
        {'data': serializer.data},
        status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_Booking(request):
    Booking.objects.get(pk = request.data.get("id", None)).delete()
    return Response(
        {'data': {"message":"success"}},
        status=status.HTTP_201_CREATED)
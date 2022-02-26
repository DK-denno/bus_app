from email import message
from math import prod
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .Serializers import UserSerializer
from .Serializers import RoleSerializer
from .Serializers import ProfileSerializer
from .Serializers import VehicleSeriaizer
from rest_framework.decorators import api_view, permission_classes
from .models import Profile, Vehicle

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
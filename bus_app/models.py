from lib2to3.pgen2 import driver
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-id']

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name="profile", on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

    class Meta:
        ordering=['-id']


class Vehicle(models.Model):
    driver = models.ForeignKey(User,
        related_name="vehicle", on_delete=models.CASCADE)
    regNumber = models.CharField(max_length=20)
    numberOfSeats = models.BigIntegerField()

    def __str__(self):
        return self.driver.username

    class Meta:
        ordering=['-id']

class Location(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-id']

class Routes(models.Model):
    locationFrom = models.ForeignKey(Location,
        related_name="routesFrom", on_delete=models.CASCADE)
    locationTo = models.ForeignKey(Location,
        related_name="routesTo", on_delete=models.CASCADE)

    def __str__(self):
        return self.locationFrom.name

    class Meta:
        ordering=['-id']

class StopsOnRoutes(models.Model):
    vehicle = models.ForeignKey(Vehicle,
        related_name="stops", on_delete=models.CASCADE)
    route = models.ForeignKey(Routes,
        related_name="stops", on_delete=models.CASCADE)
    stopLocation = models.ForeignKey(Location,
        related_name="stops", on_delete=models.CASCADE)
    stopPriority = models.BigIntegerField(null=False, blank=False)
    fare = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return self.vehicle

    class Meta:
        ordering=['-id']

class Squad(models.Model):
    vehicle = models.ForeignKey(Vehicle,
        related_name="squad", on_delete=models.CASCADE)
    regNumber = models.CharField(max_length=20)
    route = models.ForeignKey(Routes,
        related_name="squad", on_delete=models.CASCADE)
    depatureTime = models.DateTimeField(auto_now_add=True)
    arrivalTime = models.DateTimeField(auto_now_add=True)
    seatsBooked = models.BigIntegerField(null=False, blank=False, default=0)
    priority = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return self.vehicle

    class Meta:
        ordering=['-id']

class Booking(models.Model):
    passenger = models.ForeignKey(User,
        related_name="bookings", on_delete=models.CASCADE)
    squad = models.ForeignKey(Squad,
        related_name="bookings", on_delete=models.CASCADE)
    seatNumber = models.BigIntegerField(null=False, blank=False)
    stopLocation = models.ForeignKey(Location,
        related_name="bookings", on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.passenger.username

    class Meta:
        ordering=['-id']
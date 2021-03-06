from unicodedata import name
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("", views.home, name="index"),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api/token/',
        jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', views.create_user, name='create_user'),
    path('createRole/', views.create_role, name='createRole'),
    path('profile/', views.get_profile, name='profile'),
    path("createVehicle/", views.create_vehicle, name="createVehicle"),
    path("updateVehicle/", views.update_vehicle, name="updateVehicle"),
    path("deleteVehicle/", views.delete_vehicle, name="deleteVehicle"),
    path("getRoles/", views.get_roles, name="getRoles"),
    path("createLocation/", views.create_Location, name="createLocation"),
    path("getLocations/", views.get_locations, name="getLocations"),
    path("createRoutes/", views.create_Routes, name="createRoutes"),
    path("getRoutes/", views.get_Routes, name="getRoutes"),
    path("createStops/", views.create_Stops, name="createStops"),
    path("getStops/", views.get_Stops, name="getStops"),
    path("createSquads/", views.create_Squad, name="createSquads"),
    path("getSquads/", views.get_Squads, name="getSquads"),
    path("updateSquad/", views.update_squad, name="updateSquad"),
    path("createBookings/", views.create_bookings, name="createBookings"),
    path("getBookings/", views.get_Bookings, name="getBookings")
]
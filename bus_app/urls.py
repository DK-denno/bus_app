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
]
import imp
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Profile, Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token', 'first_name', 'last_name')

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)
        email = validated_data.pop('email', None)
        role = validated_data.pop('role', None)
        instance = self.Meta.model(**validated_data)
        if password is not None and first_name is not None and last_name is not None and email is not None:
            instance.set_password(password)
            instance.first_name = first_name
            instance.email = email
            instance.last_name = last_name
            prof = Profile(user=instance)
            if role is not None:
                role = Role.objects.get(pk=role)
                prof.role = role
            role = Role.objects.get(name="CLIENT")
            prof.role = role
            instance.save()
            #sve the new profile
            prof.save()
            return instance
        raise AttributeError("Either 'first_name', 'last_name' or 'email' is missing")
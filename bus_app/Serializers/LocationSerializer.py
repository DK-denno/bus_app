from rest_framework import serializers
from ..models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name',)

    def create(self, validated_data):
        name = validated_data.pop('name', None)
        instance = self.Meta.model(**validated_data)
        if name is not None:
            instance.name = name
            instance.save()
            return instance
        raise AttributeError("'name' is missing")
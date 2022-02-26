from rest_framework import serializers
from ..models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('name',)

    def create(self, validated_data):
        name = validated_data.pop('name', None)
        instance = self.Meta.model(**validated_data)
        if name is not None:
            instance.name = name
            instance.save()
            return instance
        raise AttributeError("'name' is missing")
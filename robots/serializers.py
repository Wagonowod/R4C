from rest_framework import serializers

from .models import Robot


class RobotSerializer(serializers.Serializer):
    model = serializers.CharField(min_length=2, max_length=2)
    version = serializers.CharField(min_length=2, max_length=2)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        validated_data['serial'] = validated_data['model'] + '-' + validated_data['version']
        return Robot.objects.create(**validated_data)
# todo возможно нужна валидация

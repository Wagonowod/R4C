from rest_framework import serializers

from .models import Robot


class RobotSerializer(serializers.Serializer):
    serial = serializers.SerializerMethodField()
    model = serializers.CharField(min_length=2, max_length=2)
    version = serializers.CharField(min_length=2, max_length=2)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        validated_data['serial'] = f"{validated_data['model']} - {validated_data['version']}"
        return Robot.objects.create(**validated_data)

    def get_serial(self, obj):
        return obj.serial

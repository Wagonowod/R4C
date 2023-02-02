from rest_framework import serializers


class RobotSerializer(serializers.Serializer):
    model = serializers.CharField(min_length=2, max_length=2)
    version = serializers.CharField(min_length=2, max_length=2)
    created = serializers.DateTimeField()

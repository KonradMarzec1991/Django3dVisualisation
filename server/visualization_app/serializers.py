# pylint: disable=abstract-method
"""
General serializers module
"""
from rest_framework import serializers


class DimensionSerializer(serializers.Serializer):
    """
    DimensionSerializer validates necessary coordinate values
    """
    x1 = serializers.IntegerField()
    x2 = serializers.IntegerField()
    y1 = serializers.IntegerField()
    y2 = serializers.IntegerField()
    z1 = serializers.IntegerField()
    z2 = serializers.IntegerField()


class GeometryInputSerializer(serializers.Serializer):
    """
    This serializer validates user input(geometry and plane)
    """
    PLANE_CHOICES = (
        ('XY', 'XY'),
        ('XZ', 'XZ'),
        ('YZ', 'YZ'),
        ('XYZ', 'XYZ')
    )
    geometry = DimensionSerializer(many=True)
    plane = serializers.ChoiceField(choices=PLANE_CHOICES)

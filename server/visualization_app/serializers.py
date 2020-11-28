"""
General Serializers module
"""
from rest_framework import serializers


# pylint: disable=abstract-method
class GeometryInputSerializer(serializers.Serializer):
    """
    This serializer checks request.data input
    """
    def validate_input(self):
        data = self.initial_data
        if len(data) != 2:
            raise serializers.ValidationError(
                'Dictionary contains exactly two values: `geometry` and `plane`'
            )
        if not ('geometry' in data and 'plane' in data):
            raise serializers.ValidationError(
                'Values are not in (`geometry` and `plane`)'
            )
        if data['plane'] not in ('XY', 'XZ', 'YZ', 'XYZ'):
            raise serializers.ValidationError(
                '`plane` attribute must be 2d (XY) or 3d (XYZ)'
            )
        if not isinstance(data['geometry'], list):
            raise serializers.ValidationError(
                '`geometry` attribute must be of type list'
            )
        if not all(len(dim) in range(4, 7) for dim in data['geometry']):
            raise serializers.ValidationError(
                '`geometry` attribute must contain 4 or 6 dimensions'
            )
        return

    def validate(self, attrs):
        self.validate_input()

        # do other validation...
        return super().validate(attrs)

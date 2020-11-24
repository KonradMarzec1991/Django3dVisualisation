import pytest
from visualization_app.serializers import GeometryInputSerializer


class TestGeometryInputSerializer:

    @pytest.mark.parametrize('data, error_message', [
        (
            {'Shutter': 'Island', '12 Angry ': 'Men', 'Blade': 'Runner'},
            'Dictionary contains exactly two values: `geometry` and `plane`'
        ),
        (
            {'geometry': 'geo', 'Lord of the Ring': 'The Return of the King'},
            'Values are not in (`geometry` and `plane`)'
        ),
        (
            {'geometry': 'geo', 'plane': 'Pulp Fiction'},
            '`plane` attribute must be 2d (XY) or 3d (XYZ)'
        ),
        (
            {'geometry': set(), 'plane': 'XY'},
            '`geometry` attribute must be of type list'
        ),
        (
            {'geometry': [{}, {}], 'plane': 'XYZ'},
            '`geometry` attribute must contain 4 or 6 dimensions'
        )
    ])
    def test_if_fails(self, data, error_message):
        geo_ser = GeometryInputSerializer(data=data)
        assert not geo_ser.is_valid()
        assert geo_ser.errors['non_field_errors'][0] == error_message

    def test_if_correct(self, correct_geo_input):
        geo_ser = GeometryInputSerializer(data=correct_geo_input)
        assert geo_ser.is_valid()

from visualization_app.serializers import GeometryInputSerializer


class TestGeometryInputSerializer:

    # extend in future...

    def test_if_correct(self, correct_geo_input):
        geo_ser = GeometryInputSerializer(data=correct_geo_input)
        assert geo_ser.is_valid()

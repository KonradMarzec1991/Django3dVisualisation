from visualization_app.models.geometry import Geometry


class TestGeometry:

    def test_init(self, correct_geo_input):
        geo = Geometry(correct_geo_input)
        assert geo.vis_type == 'XYZ'
        assert geo.transform.__name__ == 'visualize_3d'
        assert geo.ax.get_autoscale_on() is True

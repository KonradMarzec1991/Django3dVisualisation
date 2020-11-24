import pytest
from visualization_app.models.shapes import Rectangle, Cuboid


class TestRectangle:

    @pytest.mark.parametrize('x1, x2, y1, y2, x_dim, y_edge', [
        (2, 5, 10, 20, 3, 10),
        (2, -5, 10, -20, 7, -20),
        (-2, -5, -10, 20, 3, -10)
    ])
    def test_rectangle_creation(self, x1, x2, y1, y2, x_dim, y_edge):
        rectangle = Rectangle(x1, x2, y1, y2)
        assert rectangle.x_dim == x_dim
        assert rectangle.y_edge == y_edge


class TestCuboid:

    @pytest.mark.parametrize('x1, x2, y1, y2, z1, z2, edges, dims', [
        (
                2, 5, 10, 20, 8, 15,
                (2, 10, 8),
                (3, 10, 7)
        ),
        (
                2, -5, 10, -20, 7, -20,
                (-5, -20, -20),
                (7, 30, 27)
        ),
    ])
    def test_rectangle_creation(self, x1, x2, y1, y2, z1, z2, edges, dims):
        cub = Cuboid(x1, x2, y1, y2, z1, z2)
        assert cub.edges == edges
        assert cub.dims == dims

    def test_cuboid_data(self, cub_data):
        cub = Cuboid(1, 2, 3, 4, 5, 6)
        assert list(cub.cuboid_data()[2][1]) == [6, 6, 6, 6, 6]
        assert [list(arr) for arr in cub.cuboid_data()[0]] == cub_data

    def test_if_inherits(self):
        cub = Cuboid(1, 2, 3, 4, 5, 6)
        assert isinstance(cub, Rectangle)

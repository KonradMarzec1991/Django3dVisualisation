"""
Shapes module delivers rectangle/cuboid classes which
are used in creation of svg file
"""
import matplotlib.patches as patches
import numpy as np


class Rectangle:
    """
    Base class for plain (2d) rectangle visualization
    """
    COLOR = '#000'
    FACE_COLOR = '#e0e0d1'

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.shape = self.draw()

    @property
    def x_dim(self):
        """Calculates rectangle width"""
        return abs(self.x1 - self.x2)

    @property
    def y_dim(self):
        """Calculates rectangle length"""
        return abs(self.y1 - self.y2)

    @property
    def x_edge(self):
        """Calculates horizontal (left-bottom point of shape)"""
        return self.x1 if self.x2 > self.x1 else self.x2

    @property
    def y_edge(self):
        """Calculates edge_y (left-bottom point of shape)"""
        return self.y1 if self.y2 > self.y1 else self.y2

    def draw(self):
        """
        Gets matplotlib Rectangle object and initializes it with
        `Rectangle` instance attributes
        """
        rectangle = patches.Rectangle(
            xy=(self.x_edge, self.y_edge),
            width=self.x_dim,
            height=self.y_dim
        )

        return rectangle

    def get_figure(self):
        """
        Sets basic attributes of shape like background-/color, line-style
        """
        self.shape.set_color(Rectangle.COLOR)
        self.shape.set_facecolor(Rectangle.FACE_COLOR)
        self.shape.set_linestyle('-')
        self.shape.set_linewidth(1)

        return self.shape


class Cuboid(Rectangle):
    """
    Base class for 3d visualization
    """
    def __init__(self, x1, x2, y1, y2, z1, z2):
        super().__init__(x1, x2, y1, y2)
        self.z1 = z1
        self.z2 = z2

    @property
    def z_dim(self):
        """Calculates cuboid height"""
        return abs(self.z1 - self.z2)

    @property
    def z_edge(self):
        """Calculates cuboid down (left-bottom-down point of shape) point"""
        return self.z1 if self.z2 > self.z1 else self.z2

    @property
    def dims(self):
        """Returns tuple with width, length and height"""
        return self.x_dim, self.y_dim, self.z_dim

    @property
    def edges(self):
        """Returns edges (start point) of cuboid"""
        return self.x_edge, self.y_edge, self.z_edge

    def cuboid_data(self):
        """Calculates coordinates of all points for cuboid object"""
        l, w, h = self.dims
        pos = self.edges
        x_coord = [
            [pos[0], pos[0] + l, pos[0] + l, pos[0], pos[0]],
            [pos[0], pos[0] + l, pos[0] + l, pos[0], pos[0]],
            [pos[0], pos[0] + l, pos[0] + l, pos[0], pos[0]],
            [pos[0], pos[0] + l, pos[0] + l, pos[0], pos[0]]
        ]
        y_coord = [
            [pos[1], pos[1], pos[1] + w, pos[1] + w, pos[1]],
            [pos[1], pos[1], pos[1] + w, pos[1] + w, pos[1]],
            [pos[1], pos[1], pos[1], pos[1], pos[1]],
            [pos[1] + w, pos[1] + w, pos[1] + w, pos[1] + w, pos[1] + w]
        ]
        z_coord = [
            [pos[2], pos[2], pos[2], pos[2], pos[2]],
            [pos[2] + h, pos[2] + h, pos[2] + h, pos[2] + h, pos[2] + h],
            [pos[2], pos[2], pos[2] + h, pos[2] + h, pos[2]],
            [pos[2], pos[2], pos[2] + h, pos[2] + h, pos[2]]
        ]
        return np.array(x_coord), np.array(y_coord), np.array(z_coord)

    def draw(self, ax=None):
        """Attaches to axis object cuboid object"""
        if ax is not None:
            x, y, z = self.cuboid_data()
            ax.plot_surface(
                x, y, z,
                rstride=1,
                cstride=1,
                color=Rectangle.FACE_COLOR,
                edgecolor=Rectangle.COLOR
            )
        return AttributeError('Axis object cannot be None')

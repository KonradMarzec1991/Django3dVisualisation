"""
Module delivers transformation classes for 2d/3d visualization
"""
import os
from uuid import uuid4

import matplotlib.pyplot as plt
from django.conf import settings

from visualization_app.models.shapes import (
    Rectangle,
    Cuboid
)


class Geometry:
    """
    Delivers class which depending on type of
    visualization (2d/3d) transforms input geometry
    into matplotlib objects (ready to visualize)
    """
    def __init__(self, input_values):
        self.input_values = input_values
        self.vis_type = self.input_values['plane']
        self.figure = plt.figure()

        if self.vis_type == 'XY':
            self.ax = self.create_2d_plot()
            self.transform = self.visualize_2d
        elif self.vis_type == 'XYZ':
            self.ax = self.create_3d_plot()
            self.transform = self.visualize_3d

    @staticmethod
    def generate_path():
        """Creates path for temporary file"""
        return os.path.join(settings.UPLOADS_PATH, f'{uuid4()}.svg')

    def create_2d_plot(self):
        """Create plot for 2d visualization"""
        ax = self.figure.add_subplot(111)
        ax.grid(False)  # do not show grids
        return ax

    def create_3d_plot(self):
        """Create plot for 3d visualization"""
        ax = self.figure.gca(projection='3d')
        ax.set_aspect('auto')
        ax.grid(False)
        return ax

    # pylint: disable=too-many-locals
    def visualize_2d(self):
        """
        Loops geometry coordinates and add to ax
        object next instances of Rectangle and visualize
        """
        dims = self.input_values['geometry']
        x_start = dims[0]['x1']
        y_start = dims[0]['y1']

        # calculate maximum values for coordinates to set picture in the middle
        min_x, max_x = x_start, x_start
        min_y, max_y = y_start, y_start
        for dim in dims:
            x1, x2, y1, y2, *_ = tuple(dim.values())
            min_x, max_x = min(min_x, x1, x2), max(max_x, x1, x2)
            min_y, max_y = min(min_y, y1, y2), max(max_y, y1, y2)

            rectangle = Rectangle(x1, x2, y1, y2)
            self.ax.add_patch(rectangle.get_figure())
        plt.xlim(min_x - 50, max_x + 50)
        plt.ylim(min_y - 50, max_y + 50)

        filename = self.generate_path()
        plt.savefig(filename, transparent=True)
        return filename

    def visualize_3d(self):
        """
        Loops geometry coordinates and add to ax
        object next instances of Cuboid and visualize
        """
        dims = self.input_values['geometry']
        for dim in dims:
            cuboid = Cuboid(*tuple(dim.values()))
            cuboid.draw(ax=self.ax)

        filename = self.generate_path()
        plt.savefig(filename, transparent=True)
        return filename

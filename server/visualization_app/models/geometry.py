"""
Module delivers transformation classes for 2d/3d visualization
"""
import io

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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

        self.ax = self.create_plot()

        if self.vis_type == 'XY':
            self.transform = self.visualize_xy
        elif self.vis_type == 'XYZ':
            self.transform = self.visualize_xyz
        else:
            self.transform = self.visualize_xz_or_yz

    @staticmethod
    def create_3d_collection(rect):
        """Creates plot-like object"""
        return Poly3DCollection(rect, edgecolors='black', facecolors='#e0e0d1')

    def create_plot(self):
        """Creates appropriate plot for visualization"""
        if self.vis_type == 'XY':
            ax = self.figure.add_subplot(111)
        elif self.vis_type == 'XYZ':
            ax = self.figure.gca(projection='3d')
            ax.set_aspect('auto')
        else:
            ax = self.figure.add_subplot(111, projection='3d')
        ax.grid(False)  # do not show grids
        return ax

    # pylint: disable=too-many-locals
    def visualize_xy(self):
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

        svg_io = io.BytesIO()
        plt.savefig(svg_io, format='svg', transparent=True)
        return svg_io

    def visualize_xz_or_yz(self):
        """
        Creates XZ or YZ plots
        """
        dims = self.input_values['geometry']

        x_start = dims[0]['x1']
        y_start = dims[0]['y1']
        z_start = dims[0]['z1']

        min_x, max_x = x_start, x_start
        min_y, max_y = y_start, y_start
        min_z, max_z = z_start, z_start

        if self.vis_type == 'YZ':
            for dim in dims:
                x1, _, y1, y2, z1, z2 = tuple(dim.values())

                y, z = abs(y1 - y2), abs(z1 - z2)
                edge_y, edge_z = min(y1, y2), min(z1, z2)

                min_x, max_x = min(min_x, x1), max(max_x, x1)
                min_y, max_y = min(min_y, y1, y2), max(max_y, y1, y2)
                min_z, max_z = min(min_z, z1, z2), max(min_z, z1, z2)

                rectangle = [[
                    [x1, edge_y, edge_z],
                    [x1, edge_y, edge_z + z],
                    [x1, edge_y + y, edge_z + z],
                    [x1, edge_y + y, edge_z]
                ]]
                self.ax.add_collection3d(self.create_3d_collection(rectangle))

        elif self.vis_type == 'XZ':
            for dim in dims:
                x1, x2, y1, _, z1, z2 = tuple(dim.values())

                x, z = abs(x1 - x2), abs(z1 - z2)
                edge_x, edge_z = min(x1, x2), min(z1, z2)

                min_x, max_x = min(min_x, x1, x2), max(max_x, x1, x2)
                min_y, max_y = min(min_y, y1), max(max_y, y1)
                min_z, max_z = min(min_z, z1, z2), max(min_z, z1, z2)

                rectangle = [[
                    [edge_x, y1, edge_z],
                    [edge_x, y1, edge_z + z],
                    [edge_x + x, y1, edge_z + z],
                    [edge_x + x, y1, edge_z]
                ]]
                self.ax.add_collection3d(self.create_3d_collection(rectangle))

        self.ax.set_xlim(1.1 * min_x, 1.1 * max_x)
        self.ax.set_ylim(1.1 * min_y, 1.1 * max_y)
        self.ax.set_zlim(1.1 * min_z, 1.1 * max_z)

        svg_io = io.BytesIO()
        plt.savefig(svg_io, format='svg', transparent=True)
        return svg_io

    def visualize_xyz(self):
        """
        Loops geometry coordinates and add to ax
        object next instances of Cuboid and visualize
        """
        dims = self.input_values['geometry']
        for dim in dims:
            cuboid = Cuboid(*tuple(dim.values()))
            cuboid.draw(ax=self.ax)

        svg_io = io.BytesIO()
        plt.savefig(svg_io, format='svg', transparent=True)
        return svg_io

"""
Module delivers transformation classes for 2d/3d visualization
"""
import io
import operator
from itertools import product

import matplotlib.pyplot as plt

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
    def __init__(self, load):
        self.input_values = load['geometry']
        self.vis_type = load['plane']
        self.figure = plt.figure()

        self.ax = self.create_plot()
        if self.vis_type == 'XYZ':
            self.transform = self.visualize_3d
        else:
            self.transform = self.visualize_2d

    def create_plot(self):
        """Creates appropriate plot settings for visualization"""
        if self.vis_type == 'XYZ':
            ax = self.figure.gca(projection='3d')
            ax.set_aspect('auto')
            ax.grid(False)  # do not show grids
        else:
            ax = self.figure.add_subplot(111)
            ax.grid(True)
        return ax

    def retrieve_proper_coords(self, coord_values):
        """
        Retrieves proper coordination values from input for given orientation

        If orientation equals, for example, ZY, method creates (z1, z2, y1, y2)
        tuple and fetches data from input (dictionary in loop):

        retrieve_proper_coords({..., "y1": 9, "y2": 191, "z1": 0, "z2": 320}) ->
        (0, 320, 9, 191)

        :param coord_values: dictionary with x1, x2, ..., z2 values
        :return: tuple with coordinate values
        """
        orientation = self.vis_type.lower()
        coords = tuple(''.join(var) for var in product(orientation, '12'))
        return operator.itemgetter(*coords)(coord_values)

    def initialize_axis_parameters(self):
        """
        Delivers start values for looking minimum/maximum
        of coordinate value. Takes into account orientation of object.

        For example, if horizontal orientation of object equals Y,
        hor_start = input[0]['y1'] etc.
        """
        orientation = self.vis_type.lower()
        horizontal, vertical = tuple(orientation)

        hor_start = self.input_values[0][f'{horizontal}1']
        ver_start = self.input_values[0][f'{vertical}1']
        return hor_start, ver_start

    # pylint: disable=too-many-locals
    def visualize_2d(self):
        """
        Loops geometry coordinates and add to object next instances of Rectangle
        and saves visualization in memory as svg file

        In next iteration horizontal values (h_min, h_max) and
        vertical (v_min, v_max) values are updated in order
        to place visualization in the centre of plot
        """
        margin = 50
        hor_start, ver_start = self.initialize_axis_parameters()
        h_min, h_max = hor_start, hor_start
        v_min, v_max = ver_start, ver_start

        for dim in self.input_values:
            hor_1, hor_2, ver_1, ver_2 = self.retrieve_proper_coords(dim)

            h_min, h_max = min(h_min, hor_1, hor_2), max(h_max, hor_1, hor_2)
            v_min, v_max = min(v_min, ver_1, ver_2), max(v_max, ver_1, ver_2)

            rectangle = Rectangle(hor_1, hor_2, ver_1, ver_2)
            self.ax.add_patch(rectangle.get_figure())

        plt.xlim(h_min - margin, h_max + margin)
        plt.ylim(v_min - margin, v_max + margin)
        plt.xlabel(self.vis_type[0])  # get first letter of orientation
        plt.ylabel(self.vis_type[1])  # get second letter of orientation

        svg_io = io.BytesIO()
        plt.savefig(svg_io, format='svg', transparent=True)
        return svg_io

    def visualize_3d(self):
        """
        Loops geometry coordinates and add to ax object
        next instances of Cuboid and saves visualization
        in memory as svg file
        """
        for dim in self.input_values:
            cuboid = Cuboid(*tuple(dim.values()))
            cuboid.draw(ax=self.ax)
        svg_io = io.BytesIO()
        plt.savefig(svg_io, format='svg', transparent=True)
        return svg_io

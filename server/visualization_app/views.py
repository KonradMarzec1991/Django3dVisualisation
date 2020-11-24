"""
General ViewSet module
"""
from mimetypes import guess_type

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from visualization_app.models.geometry import Geometry
from visualization_app.serializers import GeometryInputSerializer


# pylint: disable=no-self-use,missing-class-docstring
class VisualizationViewsSet(ViewSet):

    def create(self, request):
        """
        This endpoints returns 2d/3d visualization
        for given input (geometry and plane)
        """
        serializer = GeometryInputSerializer(data=request.data)
        if serializer.is_valid():

            geo = Geometry(request.data)
            if geo.input_values['plane'] == 'XY':
                path = geo.visualize_2d()
            else:
                path = geo.visualize_3d()

            name = path.split('/')[-1]

            with open(path, 'rb') as file:
                response = HttpResponse(file, content_type=guess_type(path)[0])
                response['Content-Length'] = len(response.content)
                response['Content-Disposition'] = f'attachment; filename={name}'
                return response
        else:
            return Response(serializer.errors, status=404)

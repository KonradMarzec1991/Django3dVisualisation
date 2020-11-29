"""
General ViewSet module
"""
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
            svg_io = geo.transform()
            file = svg_io.getvalue()

            response = HttpResponse(file, content_type='image/svg+xml')
            response['Content-Length'] = len(response.content)
            response['Content-Disposition'] = 'attachment; filename=projection'
            return response
        return Response(serializer.errors, status=404)

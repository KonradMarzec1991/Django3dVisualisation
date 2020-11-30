"""
General ViewSet module
"""
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework import status

from visualization_app.models.geometry import Geometry
from visualization_app.serializers import GeometryInputSerializer


class VisualizationViewsSet(ViewSet):

    def create(self, request):
        """
        This endpoints returns 2d/3d visualization
        for given input (geometry and plane)
        """
        serializer = GeometryInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        geo = Geometry(request.data)
        svg_io = geo.transform()
        file = svg_io.getvalue()

        response = HttpResponse(
            file,
            content_type='image/svg+xml',
            status=status.HTTP_200_OK
        )
        response['Content-Length'] = len(response.content)
        response['Content-Disposition'] = 'attachment; filename=projection.svg'
        return response

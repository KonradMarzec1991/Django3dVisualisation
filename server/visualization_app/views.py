"""
General ViewSet module
"""
from mimetypes import guess_type
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from visualization_app.figure import DataVisualize
from visualization_app.serializers import DataSerializer


# pylint: disable=no-self-use,missing-class-docstring
class VisualizationViewsSet(ViewSet):

    def create(self, request):
        """
        This endpoints returns 2d/3d visualization
        for given input (geometry and plane)
        """
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            vis_obj = DataVisualize(request.data)
            if vis_obj.input_values['plane'] == 'XY':
                path = vis_obj.visualize_2d()
            else:
                path = vis_obj.visualize_3d()
            name = path.split('/')[-1]

            with open(path, 'rb') as file:
                response = HttpResponse(file, content_type=guess_type(path)[0])
                response['Content-Length'] = len(response.content)
                response['Content-Disposition'] = f'attachment; filename={name}'
                return response
        else:
            return Response(serializer.errors, status=404)

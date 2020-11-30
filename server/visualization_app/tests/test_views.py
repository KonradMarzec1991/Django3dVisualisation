from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status


class TestVisualizationViewsSet:

    def test_status(self, correct_geo_input):
        client = APIClient()
        response = client.post(
            reverse('projection-list'),
            data=correct_geo_input,
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK
        assert response._headers['content-type'][1] == 'image/svg+xml'

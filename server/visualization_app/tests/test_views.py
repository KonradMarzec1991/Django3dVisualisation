from rest_framework.test import APIClient


class TestVisualizationViewsSet:

    PATH = '/api/visualize/'

    def test_status(self, correct_geo_input):
        client = APIClient()
        response = client.post(self.PATH, data=correct_geo_input, format='json')
        assert response.status_code == 200
        assert response._headers['content-type'][1] == 'image/svg+xml'

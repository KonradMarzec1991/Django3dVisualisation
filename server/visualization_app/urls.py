"""
General visualization_app Urls module
"""
from rest_framework import routers

from .views import VisualizationViewsSet

router = routers.SimpleRouter()

router.register(
    prefix=r'projection',
    viewset=VisualizationViewsSet,
    basename='projection'
)

urlpatterns = router.urls

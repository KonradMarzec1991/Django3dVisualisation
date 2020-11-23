"""
General Urls module
"""
from django.contrib import admin
from django.urls import path, include

from visualization_app.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

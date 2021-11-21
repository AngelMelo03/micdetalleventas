from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'detalleventas', views.DetalleventasViewSet, basename = 'detalleventas')


urlpatterns = [
    path('', include(router.urls)),

]

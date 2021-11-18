from rest_framework import viewsets
from .models import *
from .serializer import *


# Create your views here.
class DetalleventasViewSet(viewsets.ModelViewSet):
    queryset = Detalleventas.objects.all()
    serializer_class = DetalleventasSerializers
from rest_framework.generics import(
#ListCreateAPIView,
#RetrieveUpdateDestroyAPIView,
#RetrieveUpdateAPIView,
#CreateAPIView,
#ListAPIView,
RetrieveAPIView,
#UpdateAPIView,
#DestroyAPIView,
)
from ..models import Service
from .serializers import ServiceSerializer

class ServiceRetrieveView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = []
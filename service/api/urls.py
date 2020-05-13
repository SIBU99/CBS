from django.urls import path
from .views import ServiceRetrieveView

urlpatterns = [
    path("bus/<int:pk>/", ServiceRetrieveView.as_view(), name="Bus-detail"),
]

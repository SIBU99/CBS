from django.urls import path
from .views import (
    StudentCreate,
    StudentRetrieveUpdateDestroyView,
    Login,
    ChangeCreditial,
)

urlpatterns = [
    path("student/", StudentCreate.as_view(), name="student-create"),
    path("student/<int:pk>/", StudentRetrieveUpdateDestroyView.as_view(), name="student-detail"),
    path("login/", Login.as_view(), name="login"),
    path("ChangeCreditial/", ChangeCreditial.as_view(), name="change-credits")
]

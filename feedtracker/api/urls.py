# api/urls.py
from django.urls import path
from .views import RegistroListCreate, RegistroDetail, RegistroUltimo

urlpatterns = [
    path("registros/", RegistroListCreate.as_view(), name="registro-list-create"),
    path("registros/<int:index>/", RegistroDetail.as_view(), name="registro-detail"),
    path("registros/ultimo/", RegistroUltimo.as_view(), name="registro-ultimo"),
]

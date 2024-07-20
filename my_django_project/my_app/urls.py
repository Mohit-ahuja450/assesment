from django.urls import path
from . import views

urlpatterns = [
    path('api/endpoint1/', views.api_endpoint_1),
    path('api/endpoint2/', views.api_endpoint_2),
]

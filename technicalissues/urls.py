from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('technicalissues/', views.technicalissues, name='technicalissues'),
    path('technicalissues/<str:device_type>/', views.device_guide, name='device_guide'),
]
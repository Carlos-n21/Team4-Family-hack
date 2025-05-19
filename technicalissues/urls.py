from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('technicalissues/', views.technicalissues, name='technicalissues'),
]
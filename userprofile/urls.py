from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.custom_logout, name='logout_alternate'),
]

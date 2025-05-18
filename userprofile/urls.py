from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.custom_logout, name='logout_alternate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

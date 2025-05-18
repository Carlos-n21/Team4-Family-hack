from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.custom_logout, name='logout_alternate'),
    path('delete/', views.delete_account, name='delete_account'),
    path('toggle_bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
    path('bookmarks/', views.bookmarks_view, name='bookmarks'),
    path('remove_bookmark/<int:pk>/', views.remove_bookmark, name='remove_bookmark'),
]

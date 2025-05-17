from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
    path("chat/api/", views.chat_api, name="chat_api"),
]
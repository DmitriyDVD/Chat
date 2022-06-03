from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mypage', views.mypage, name='mypage'),
    path('messenger', views.messenger, name='messenger'),
    path('chat', views.chat, name='chat.py'),
]

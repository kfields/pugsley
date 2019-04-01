from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<slug:slug>/', views.post, name='post'),
    path('users/<slug:username>/', views.user, name='user'),
]
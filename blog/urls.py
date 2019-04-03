from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('calendar', views.calendar, name='calendar'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('posts/<slug:slug>/', views.post, name='post'),
    path('users/<slug:username>/', views.user, name='user'),
]
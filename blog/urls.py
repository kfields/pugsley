from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('posts/<slug:slug>/', views.post, name='post'),
    path('profiles/<slug:username>/edit', views.profile_edit, name='profile_edit'),
    path('profiles/<slug:username>/', views.profile, name='profile'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myaccount, name='myaccount'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.LogIn.as_view(), name='login'),
]
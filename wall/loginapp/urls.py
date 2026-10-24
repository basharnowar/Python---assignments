from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('create_user/', views.create_user),
    path('check_login/', views.check_login),
    path('logout/', views.logout)
]

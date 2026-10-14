from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.safe),
    path('', views.root),
    path('blogs/', views.safe),
    path('blogs/new/', views.new ),
    path('blogs/create/', views.create),
    path('blogs/<number>/', views.numbers),
    # path('blogs/<nums>/', views.nums),
    path('blogs/<number>/destroy', views.destroy),
]
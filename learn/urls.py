from django.urls import path
from . import views

urlpatterns = [
    path('hello1', views.hello1),
    path('hello/', views.hello),
]

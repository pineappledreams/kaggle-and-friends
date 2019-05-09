from django.urls import path
from hello_django import views

urlpatterns = [
    path("", views.home, name="home")
]


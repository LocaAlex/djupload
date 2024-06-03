from django.urls import path

from . import views

app_name = "upload"
urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("login", views.login, name="login"),
]

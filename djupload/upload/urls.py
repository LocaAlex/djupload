from django.urls import path

from . import views

app_name = "upload"
urlpatterns = [
    path("", views.djupload, name="djupload"),
    path("home", views.index, name="index"),
    path("about", views.about, name="about"),
    path("login", views.login, name="login"),
]

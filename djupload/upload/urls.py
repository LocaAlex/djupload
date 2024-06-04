from django.urls import path

from . import views

app_name = "upload"
urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path('download/<str:file_uuid>/', views.download_file, name='download_file'),
    path('delete/<uuid:file_uuid>/', views.delete_file, name='delete_file'),
    path("about", views.about, name="about"),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
]

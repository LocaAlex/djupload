from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'upload/index.html')


def home(request):
    return render(request, "upload/home.html")


def about(request):
    return render(request, "upload/about.html")


def login(request):
    return render(request, "upload/login.html")
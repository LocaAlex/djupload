from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'upload/index.html')

def about(request):
    return render(request, "upload/about.html")

def login(request):
    return render(request, "upload/login.html")

def djupload(request):
    return render(request, "upload/djupload.html")

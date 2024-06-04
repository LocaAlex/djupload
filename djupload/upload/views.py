from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserFile
from .forms import SignupForm, LoginForm, FileUploadForm

def index(request):
    return render(request, 'upload/index.html')

@login_required(login_url='upload:login')
def home(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            messages.success(request, 'File uploaded successfully.')
            return redirect('upload:home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = FileUploadForm()
    
    # Fetch the files for the logged-in user
    files = UserFile.objects.filter(user=request.user)
    
    return render(request, 'upload/home.html', {'form': form, 'files': files})

def about(request):
    return render(request, "upload/about.html")

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('upload:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignupForm()
    return render(request, 'upload/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('upload:home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = LoginForm()
    return render(request, 'upload/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('upload:index')
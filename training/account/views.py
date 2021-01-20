from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .forms import UserForm
from .models import Client
from django.shortcuts import redirect


# Create your views here.
def dashboard(request):
    return render(request, "user/dashboard.html")


def signup_view(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            client = form.save()
            login(request, client)
            return redirect('train:index')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            client = form.get_user()
            login(request, client)
            return redirect('train:index')
        else:
            print(form.error_messages)
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('train:index')

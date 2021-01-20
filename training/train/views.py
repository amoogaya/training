from django.shortcuts import render, redirect
from .forms import RequestRegisterForm
from handle.models import RegisterRequestState
from .models import RegisterRequest


# Create your views here.

def index_view(request):
    return render(request, "train/base.html")


def add_request(request):
    if request.method == 'POST':
        form = RequestRegisterForm(request.POST)

        if form.is_valid():
            register_request = form.save()
            request_state = RegisterRequestState.objects.create(
                register_request=register_request,
                flag='pending_employee_review'
            )

            return redirect('train:index')
    else:
        form = RequestRegisterForm()
    return render(request, 'train/add_request.html', {'form': form})

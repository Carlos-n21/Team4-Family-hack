from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.http import require_GET
from .forms import SignUpForm

@login_required
def profile_view(request):
    return render(request, 'userprofile/profile.html', {
        'user': request.user
    })

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@require_GET
def custom_logout(request):
    logout(request)
    # First try to redirect to home, if that fails then to login
    try:
        return redirect('home')
    except:
        return redirect('login')
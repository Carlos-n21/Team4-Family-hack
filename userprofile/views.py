from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
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
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.hashers import check_password
from .forms import SignUpForm, ProfileImageForm
from .models import Profile
from django.http import JsonResponse
from .models import GuideBookmark
import json

@login_required
def profile_view(request):
    # Create profile if it doesn't exist
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        # Check if the user wants to remove their profile image
        if 'remove_image' in request.POST:
            # Clear the image field
            if request.user.profile.image:
                request.user.profile.image = None
                request.user.profile.save()
                messages.success(request, 'Your profile photo has been removed!')
            return redirect('profile')
        else:
            # Handle image upload
            form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('profile')
    else:
        form = ProfileImageForm(instance=request.user.profile)

    bookmarks = GuideBookmark.objects.filter(user=request.user)
    return render(request, 'userprofile/profile.html', {
        'user': request.user,
        'form': form,
        'bookmarks': bookmarks,
    })

@login_required
@require_POST
def delete_account(request):
    # Verify the user's password for security
    password = request.POST.get('password')
    user = request.user
    
    if not check_password(password, user.password):
        messages.error(request, 'Incorrect password. Account deletion failed.')
        return redirect('profile')
    
    # If password is correct, delete the user
    try:
        # This will delete the user and its related profile due to CASCADE
        user.delete()
        messages.success(request, 'Your account has been permanently deleted.')
        return redirect('home')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('profile')

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
    
@login_required
@require_POST
def toggle_bookmark(request):
    # Get data from JSON payload instead of POST
    data = json.loads(request.body)
    device_type = data.get('device_type')
    guide_type = data.get('guide_type')
    guide_key = data.get('guide_key')

    if not all([device_type, guide_type, guide_key]):
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    try:
        # Use get_or_create with all required fields
        bookmark, created = GuideBookmark.objects.get_or_create(
            user=request.user,
            device_type=device_type,
            guide_type=guide_type,
            guide_key=guide_key
        )
        
        if not created:
            bookmark.delete()
            status = 'removed'
        else:
            status = 'added'
            
        return JsonResponse({'status': status})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@login_required
def bookmarks_view(request):
    bookmarks = GuideBookmark.objects.filter(user=request.user)
    return render(request, 'userprofile/bookmarks.html', {
        'bookmarks': bookmarks,
    })

@login_required
def remove_bookmark(request, pk):
    if request.method == 'POST':
        bookmark = get_object_or_404(GuideBookmark, pk=pk, user=request.user)
        bookmark.delete()
    return redirect('bookmarks')
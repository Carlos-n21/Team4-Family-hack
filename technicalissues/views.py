from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from userprofile.models import GuideBookmark

def home(request):
    return render(request, "home.html")

def technicalissues(request):
    return render(request, "technicalissues.html")

@login_required
def device_guide(request, device_type):
    """
    View to handle device-specific guides, with bookmark support
    Args:
        device_type: The type of device (mobile, laptop, tv, etc.)
    """
    # Device types and their display names
    device_info = {
        'mobile': {
            'name': 'Mobile Devices',
            'icon': 'mobile.png',
            'description': 'Get help with your smart phones and tablets'
        },
        'laptop': {
            'name': 'Laptops/Desktops',
            'icon': 'laptop.png',
            'description': 'Get help with your laptops and desktops'
        },
        'tv': {
            'name': 'TV',
            'icon': 'tv.png',
            'description': 'Get help with your TVs'
        },
        'router': {
            'name': 'Routers',
            'icon': 'router.jpg',
            'description': 'Get help with your Routers'
        },
        'smartmeter': {
            'name': 'Smart Meters',
            'icon': 'smartmeter.jpg',
            'description': 'Get help with your Smart Meters'
        },
        'printer': {
            'name': 'Printers',
            'icon': 'printer.png',
            'description': 'Get help with your Printers'
        }
    }
    
    if request.user.is_authenticated:
        user_bookmarks = GuideBookmark.objects.filter(
            user=request.user, 
            device_type=device_type
        )
        # Create dictionary with composite keys
        bookmarks = {
            f"{bm.guide_type}_{bm.guide_key}": True 
            for bm in user_bookmarks
        }
    else:
        bookmarks = {}

    context = {
        'device_type': device_type,
        'device_info': device_info.get(device_type, {}),
        'bookmarks': bookmarks,
    }
    return render(request, "device_guide.html", context)

from django.shortcuts import render

def home(request):
    return render(request, "home.html") 

def technicalissues(request):
    return render(request, "technicalissues.html")

def device_guide(request, device_type):
    """
    View to handle device-specific guides
    
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
    
    context = {
        'device_type': device_type,
        'device_info': device_info.get(device_type, {})
    }
    
    return render(request, "device_guide.html", context)
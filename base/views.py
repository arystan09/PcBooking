import math
from django.http import JsonResponse
from django.shortcuts import redirect, render
import requests
from django.conf import settings
from selenium import webdriver
from .models import Club
from .forms import *
from django.contrib.auth import authenticate,login,logout

#example of full address
#
def geocode_address(address):
    api_key = settings.OPENCAGE_API_KEY
    url = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={api_key}"
    
    response = requests.get(url)
    data = response.json()

    if data['results']:
        latitude = data['results'][0]['geometry']['lat']
        longitude = data['results'][0]['geometry']['lng']
        return latitude, longitude
    else:
        return None, None
    

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def get_nearest_clubs(request):
    user_lat = float(request.GET.get('latitude'))
    user_lon = float(request.GET.get('longitude'))

    clubs = Club.objects.all()
    club_distances = []

    for club in clubs:
        # Combine address, city, and country for geocoding
        full_address = f"{club.address}, {club.city}, {club.country}"
        lat, lon = geocode_address(full_address)

        if lat is not None and lon is not None:
            # Calculate the distance between user and club
            distance = haversine(user_lat, user_lon, lat, lon)
            club_distances.append({
                'name': club.name,
                'address': club.address,
                'city': club.city,
                'country': "Kazakhstan",
                'distance': round(distance, 2)
            })

    # Sort by distance
    sorted_clubs = sorted(club_distances, key=lambda x: x['distance'])

    return JsonResponse(sorted_clubs, safe=False)

def list_computer_clubs(request):
    clubs = Club.objects.all()
    return render(request, 'base/allcompclubs.html', {'clubs': clubs})

def home(request):
    return render(request, 'base/home.html')


def book(request):
    return render(request, 'base/book.html')
    

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'base/register.html', {'form': form})

def login_user(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'base/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')

def user_profile(request):
    return render(request, 'base/user_profile.html')

def parse_2gis():
    search_query = "Компьютерный клуб"
    url = f"https://2gis.kz/astana/search/{search_query}"
    driver = webdriver.Chrome()
    driver.get(url)
    pass
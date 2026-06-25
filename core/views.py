from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, City, Business

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    categories = Category.objects.all()[:12]
    popular_cities = City.objects.filter(is_popular=True)[:10]
    featured_businesses = Business.objects.filter(is_verified=True).order_by('-rating')[:8]
    context = {
        'categories': categories,
        'popular_cities': popular_cities,
        'featured_businesses': featured_businesses,
    }
    return render(request, 'home.html', context)

@login_required
def search(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    city_id = request.GET.get('city', '')
    
    businesses = Business.objects.all()
    
    if query:
        businesses = businesses.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(address__icontains=query)
        )
    
    if category_id:
        businesses = businesses.filter(category_id=category_id)
    
    if city_id:
        businesses = businesses.filter(city_id=city_id)
    
    categories = Category.objects.all()
    cities = City.objects.all()
    
    context = {
        'businesses': businesses,
        'categories': categories,
        'cities': cities,
        'query': query,
        'selected_category': category_id,
        'selected_city': city_id,
    }
    return render(request, 'search.html', context)

@login_required
def business_detail(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    return render(request, 'business_detail.html', {'business': business})

@login_required
def category_listings(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    businesses = Business.objects.filter(category=category)
    return render(request, 'category_listings.html', {'category': category, 'businesses': businesses})

@login_required
def city_listings(request, city_id):
    city = get_object_or_404(City, id=city_id)
    businesses = Business.objects.filter(city=city)
    return render(request, 'city_listings.html', {'city': city, 'businesses': businesses})
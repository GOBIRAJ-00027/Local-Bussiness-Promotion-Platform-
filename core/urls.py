from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('business/<int:business_id>/', views.business_detail, name='business_detail'),
    path('category/<int:category_id>/', views.category_listings, name='category_listings'),
    path('city/<int:city_id>/', views.city_listings, name='city_listings'),
]
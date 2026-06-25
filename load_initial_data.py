#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justdial_project.settings')
django.setup()

from core.models import Category, City, Business


def load_initial_data():
    # Load Categories
    categories_data = [
        {'name': 'Restaurants', 'icon': 'restaurant'},
        {'name': 'Hospitals', 'icon': 'hospital'},
        {'name': 'Hotels', 'icon': 'building'},
        {'name': 'Schools', 'icon': 'book'},
        {'name': 'Banks', 'icon': 'bank'},
        {'name': 'Pharmacies', 'icon': 'capsule'},
        {'name': 'Salons', 'icon': 'scissors'},
        {'name': 'Gyms', 'icon': 'heart-pulse'},
        {'name': 'Auto Repair', 'icon': 'wrench'},
        {'name': 'Pet Shops', 'icon': 'cat'},
        {'name': 'Electronics', 'icon': 'tv'},
        {'name': 'Clothing', 'icon': 'bag'},
    ]

    category_objects = {}
    for cat_data in categories_data:
        cat, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'icon': cat_data['icon']}
        )
        category_objects[cat_data['name']] = cat
        if created:
            print(f"Created category: {cat.name}")
        else:
            print(f"Category already exists: {cat.name}")

    # Load Cities
    cities_data = [
        {'name': 'Chennai', 'state': 'Tamil Nadu', 'is_popular': True},
        {'name': 'Coimbatore', 'state': 'Tamil Nadu', 'is_popular': True},
        {'name': 'Madurai', 'state': 'Tamil Nadu', 'is_popular': True},
        {'name': 'Trichy', 'state': 'Tamil Nadu', 'is_popular': True},
        {'name': 'Salem', 'state': 'Tamil Nadu', 'is_popular': True},
        {'name': 'Tirunelveli', 'state': 'Tamil Nadu', 'is_popular': False},
        {'name': 'Erode', 'state': 'Tamil Nadu', 'is_popular': False},
        {'name': 'Vellore', 'state': 'Tamil Nadu', 'is_popular': False},
    ]

    city_objects = {}
    for city_data in cities_data:
        city, created = City.objects.get_or_create(
            name=city_data['name'],
            defaults={'state': city_data['state'], 'is_popular': city_data['is_popular']}
        )
        city_objects[city_data['name']] = city
        if created:
            print(f"Created city: {city.name}")
        else:
            print(f"City already exists: {city.name}")

    # Load Businesses
    businesses_data = [
        {
            'name': 'Saravana Bhavan',
            'category': 'Restaurants',
            'city': 'Chennai',
            'address': 'Anna Salai, Teynampet',
            'phone': '044-24334444',
            'email': 'info@saravanabhavan.com',
            'website': 'https://www.saravanabhavan.com',
            'rating': 4.5,
            'review_count': 1250,
            'description': 'Famous South Indian vegetarian restaurant chain known for authentic Tamil cuisine and delicious dosas.',
            'is_verified': True,
            'is_open_24x7': True,
        },
        {
            'name': 'Apollo Hospitals',
            'category': 'Hospitals',
            'city': 'Chennai',
            'address': '21 Greams Lane, Thousand Lights',
            'phone': '044-28290200',
            'email': 'contact@apollohospitals.com',
            'website': 'https://www.apollohospitals.com',
            'rating': 4.8,
            'review_count': 3500,
            'description': 'One of India\'s leading healthcare providers with state-of-the-art facilities and expert doctors.',
            'is_verified': True,
            'is_open_24x7': True,
        },
        {
            'name': 'Taj Coromandel',
            'category': 'Hotels',
            'city': 'Chennai',
            'address': '37 Magsaysay Road, Nungambakkam',
            'phone': '044-66260000',
            'email': 'reservations@tajhotels.com',
            'website': 'https://www.tajhotels.com',
            'rating': 4.7,
            'review_count': 2100,
            'description': 'Luxury 5-star hotel offering world-class amenities and fine dining experiences.',
            'is_verified': True,
            'is_open_24x7': False,
        },
        {
            'name': 'Chettinad Mess',
            'category': 'Restaurants',
            'city': 'Chennai',
            'address': 'T. Nagar, Near Pondy Bazaar',
            'phone': '044-28123456',
            'email': '',
            'website': '',
            'rating': 4.2,
            'review_count': 850,
            'description': 'Authentic Chettinad cuisine with spicy and flavorful dishes. Popular for lunch and dinner.',
            'is_verified': True,
            'is_open_24x7': False,
        },
        {
            'name': 'PSG Hospitals',
            'category': 'Hospitals',
            'city': 'Coimbatore',
            'address': 'Avinashi Road, Peelamedu',
            'phone': '0422-2570170',
            'email': 'info@psghospitals.com',
            'website': 'https://www.psghospitals.com',
            'rating': 4.6,
            'review_count': 1800,
            'description': 'Multi-specialty hospital with advanced medical facilities and experienced healthcare professionals.',
            'is_verified': True,
            'is_open_24x7': True,
        },
        {
            'name': 'Sangam Hotel',
            'category': 'Hotels',
            'city': 'Madurai',
            'address': '77 Alagar Koil Road, K. K. Nagar',
            'phone': '0452-2534444',
            'email': 'reservations@sangamhotel.com',
            'website': 'https://www.sangamhotel.com',
            'rating': 4.4,
            'review_count': 950,
            'description': 'Premium hotel in Madurai with comfortable rooms and excellent traditional hospitality.',
            'is_verified': True,
            'is_open_24x7': False,
        },
        {
            'name': 'St. Joseph\'s College',
            'category': 'Schools',
            'city': 'Chennai',
            'address': 'Trichy Road, Tiruchirappalli',
            'phone': '0431-2764400',
            'email': 'principal@stjosephs.edu',
            'website': 'https://www.stjosephs.edu',
            'rating': 4.5,
            'review_count': 650,
            'description': 'Premier educational institution offering quality education with modern infrastructure.',
            'is_verified': True,
            'is_open_24x7': False,
        },
        {
            'name': 'State Bank of India',
            'category': 'Banks',
            'city': 'Chennai',
            'address': 'Anna Salai, Mount Road',
            'phone': '044-28410000',
            'email': 'contact@sbi.co.in',
            'website': 'https://www.sbi.co.in',
            'rating': 3.8,
            'review_count': 420,
            'description': 'Main branch of State Bank of India with full banking services and ATM facilities.',
            'is_verified': True,
            'is_open_24x7': False,
        },
        {
            'name': 'MedPlus Pharmacy',
            'category': 'Pharmacies',
            'city': 'Coimbatore',
            'address': 'RS Puram, Coimbatore',
            'phone': '0422-2567890',
            'email': 'help@medplusindia.com',
            'website': 'https://www.medplusindia.com',
            'rating': 4.3,
            'review_count': 320,
            'description': 'Leading pharmacy chain with wide range of medicines and health products.',
            'is_verified': True,
            'is_open_24x7': True,
        },
        {
            'name': 'Lakme Salon',
            'category': 'Salons',
            'city': 'Chennai',
            'address': 'Express Avenue Mall, Royapettah',
            'phone': '044-28123456',
            'email': '',
            'website': '',
            'rating': 4.1,
            'review_count': 280,
            'description': 'Premium beauty salon offering hair styling, skincare, and bridal makeup services.',
            'is_verified': True,
            'is_open_24x7': False,
        },
        {
            'name': 'Fitness First Gym',
            'category': 'Gyms',
            'city': 'Chennai',
            'address': 'Nungambakkam, Chennai',
            'phone': '044-28234567',
            'email': 'chennai@fitnessfirstindia.com',
            'website': 'https://www.fitnessfirstindia.com',
            'rating': 4.4,
            'review_count': 560,
            'description': 'Modern gym with latest equipment, personal trainers, and group fitness classes.',
            'is_verified': True,
            'is_open_24x7': True,
        },
        {
            'name': 'Maruti Service Center',
            'category': 'Auto Repair',
            'city': 'Coimbatore',
            'address': 'Avinashi Road, Coimbatore',
            'phone': '0422-2334567',
            'email': 'service@maruti.co.in',
            'website': 'https://www.maruti.co.in',
            'rating': 4.2,
            'review_count': 890,
            'description': 'Authorized Maruti Suzuki service center with expert technicians and genuine spare parts.',
            'is_verified': True,
            'is_open_24x7': False,
        },
    ]

    for biz_data in businesses_data:
        biz, created = Business.objects.get_or_create(
            name=biz_data['name'],
            defaults={
                'category': category_objects[biz_data['category']],
                'city': city_objects[biz_data['city']],
                'address': biz_data['address'],
                'phone': biz_data['phone'],
                'email': biz_data['email'],
                'website': biz_data['website'],
                'rating': biz_data['rating'],
                'review_count': biz_data['review_count'],
                'description': biz_data['description'],
                'is_verified': biz_data['is_verified'],
                'is_open_24x7': biz_data['is_open_24x7'],
            }
        )
        if created:
            print(f"Created business: {biz.name}")
        else:
            print(f"Business already exists: {biz.name}")

    print("Initial data load complete!")


if __name__ == '__main__':
    load_initial_data()

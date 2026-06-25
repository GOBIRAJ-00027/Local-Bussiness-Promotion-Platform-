#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infohub_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create superuser with username josh and password 5050
if not User.objects.filter(username='josh').exists():
    User.objects.create_superuser('josh', 'josh@example.com', '5050')
    print("Superuser 'josh' created successfully!")
else:
    print("Superuser 'josh' already exists!")
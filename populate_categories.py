import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoftBoyCrownProject.settings')
django.setup()

from SoftBoyCrownApp.models import Category

# Define categories for a clothing store
categories = [
    {
        'name': 'T-Shirts',
        'description': 'Comfortable and stylish t-shirts for everyday wear.'
    },
    {
        'name': 'Hoodies',
        'description': 'Warm and cozy hoodies for cooler weather.'
    },
    {
        'name': 'Jackets',
        'description': 'Stylish jackets to complete your outfit.'
    },
    {
        'name': 'Accessories',
        'description': 'Hats, bags, and other accessories to complement your style.'
    },
    {
        'name': 'Limited Edition',
        'description': 'Special limited edition items with unique designs.'
    },
    {
        'name': 'Streetwear',
        'description': 'Urban fashion inspired by street culture.'
    },
]

# Add categories to the database
for category_data in categories:
    category, created = Category.objects.get_or_create(
        name=category_data['name'],
        defaults={'description': category_data['description']}
    )
    
    if created:
        print(f"Created category: {category.name}")
    else:
        print(f"Category already exists: {category.name}")

print("\nCategories in database:")
for category in Category.objects.all():
    print(f"- {category.name}: {category.description}")
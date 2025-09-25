import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoftBoyCrownProject.settings')
django.setup()

from SoftBoyCrownApp.models import Color, Size, Product, Category

def populate_colors():
    """Populate the database with colors"""
    colors = [
        {"name": "Black", "hex_code": "#000000"},
        {"name": "White", "hex_code": "#FFFFFF"},
        {"name": "Red", "hex_code": "#FF0000"},
        {"name": "Blue", "hex_code": "#0000FF"},
        {"name": "Green", "hex_code": "#008000"},
        {"name": "Yellow", "hex_code": "#FFFF00"},
        {"name": "Purple", "hex_code": "#800080"},
        {"name": "Pink", "hex_code": "#FFC0CB"},
        {"name": "Gray", "hex_code": "#808080"},
        {"name": "Brown", "hex_code": "#A52A2A"},
    ]
    
    for color_data in colors:
        color, created = Color.objects.get_or_create(
            name=color_data["name"],
            defaults={"hex_code": color_data["hex_code"]}
        )
        if created:
            print(f"Created color: {color.name}")
        else:
            print(f"Color already exists: {color.name}")
    
    return Color.objects.all()

def populate_sizes():
    """Populate the database with sizes"""
    sizes = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
    
    for size_name in sizes:
        size, created = Size.objects.get_or_create(name=size_name)
        if created:
            print(f"Created size: {size.name}")
        else:
            print(f"Size already exists: {size.name}")
    
    return Size.objects.all()

def populate_categories():
    """Ensure categories exist"""
    categories = [
        {"name": "T-Shirts", "description": "Comfortable and stylish t-shirts"},
        {"name": "Hoodies", "description": "Warm and cozy hoodies"},
        {"name": "Pants", "description": "Stylish pants for all occasions"},
        {"name": "Accessories", "description": "Stylish accessories to complete your look"}
    ]
    
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data["name"],
            defaults={"description": category_data["description"]}
        )
        if created:
            print(f"Created category: {category.name}")
        else:
            print(f"Category already exists: {category.name}")
    
    return Category.objects.all()

def populate_products(colors, sizes, categories):
    """Populate the database with products"""
    products_data = [
        {
            "name": "Classic Black Tee",
            "price": 29.99,
            "slash_price": 39.99,
            "category": "T-Shirts",
            "in_stock": 50,
            "description": "<p>Our classic black tee is made from 100% organic cotton. Perfect for any occasion.</p>",
            "colors": ["Black", "White"],
            "sizes": ["S", "M", "L", "XL"]
        },
        {
            "name": "Vintage Logo Hoodie",
            "price": 59.99,
            "slash_price": 69.99,
            "category": "Hoodies",
            "in_stock": 30,
            "description": "<p>Stay warm and stylish with our vintage logo hoodie. Features a soft inner lining and adjustable hood.</p>",
            "colors": ["Black", "Gray", "Blue"],
            "sizes": ["M", "L", "XL", "XXL"]
        },
        {
            "name": "Slim Fit Jeans",
            "price": 49.99,
            "slash_price": 59.99,
            "category": "Pants",
            "in_stock": 25,
            "description": "<p>Our slim fit jeans offer both comfort and style. Made with premium denim that lasts.</p>",
            "colors": ["Blue", "Black"],
            "sizes": ["S", "M", "L", "XL"]
        },
        {
            "name": "Graphic Print Tee",
            "price": 34.99,
            "slash_price": 44.99,
            "category": "T-Shirts",
            "in_stock": 40,
            "description": "<p>Express yourself with our unique graphic print tee. Each design is exclusive to our brand.</p>",
            "colors": ["White", "Black", "Red"],
            "sizes": ["XS", "S", "M", "L", "XL"]
        },
        {
            "name": "Zip-Up Hoodie",
            "price": 54.99,
            "slash_price": 64.99,
            "category": "Hoodies",
            "in_stock": 20,
            "description": "<p>Our zip-up hoodie combines functionality with style. Features deep pockets and a durable zipper.</p>",
            "colors": ["Black", "Gray", "Green"],
            "sizes": ["S", "M", "L", "XL", "XXL"]
        },
        {
            "name": "Cargo Pants",
            "price": 44.99,
            "slash_price": 54.99,
            "category": "Pants",
            "in_stock": 15,
            "description": "<p>Our cargo pants are perfect for those who need extra storage without sacrificing style.</p>",
            "colors": ["Brown", "Green", "Black"],
            "sizes": ["M", "L", "XL", "XXL"]
        },
        {
            "name": "Beanie Hat",
            "price": 19.99,
            "slash_price": 24.99,
            "category": "Accessories",
            "in_stock": 60,
            "description": "<p>Keep your head warm with our stylish beanie hat. Made from soft, high-quality materials.</p>",
            "colors": ["Black", "Gray", "Red", "Blue"],
            "sizes": ["One Size"]
        },
        {
            "name": "Leather Belt",
            "price": 29.99,
            "slash_price": 39.99,
            "category": "Accessories",
            "in_stock": 35,
            "description": "<p>Complete your look with our premium leather belt. Durable and timeless.</p>",
            "colors": ["Black", "Brown"],
            "sizes": ["S", "M", "L", "XL"]
        }
    ]
    
    # Create a mapping of category names to objects
    category_map = {category.name: category for category in categories}
    color_map = {color.name: color for color in colors}
    size_map = {size.name: size for size in sizes}
    
    for product_data in products_data:
        # Get the category object
        category = category_map.get(product_data["category"])
        if not category:
            print(f"Category {product_data['category']} not found, skipping product {product_data['name']}")
            continue
        
        # Create or update the product
        product, created = Product.objects.get_or_create(
            name=product_data["name"],
            defaults={
                "price": product_data["price"],
                "slash_price": product_data["slash_price"],
                "category": category,
                "in_stock": product_data["in_stock"],
                "description": product_data["description"],
                "is_active": True
            }
        )
        
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product already exists: {product.name}")
            # Update the product
            product.price = product_data["price"]
            product.slash_price = product_data["slash_price"]
            product.category = category
            product.in_stock = product_data["in_stock"]
            product.description = product_data["description"]
            product.save()
        
        # Add colors to the product
        for color_name in product_data["colors"]:
            color = color_map.get(color_name)
            if color:
                product.colors.add(color)
        
        # Add sizes to the product
        for size_name in product_data["sizes"]:
            size = size_map.get(size_name)
            if size:
                product.sizes.add(size)

def main():
    """Main function to populate the database"""
    print("Starting database population...")
    
    # Populate colors
    colors = populate_colors()
    print(f"Total colors: {colors.count()}")
    
    # Populate sizes
    sizes = populate_sizes()
    print(f"Total sizes: {sizes.count()}")
    
    # Populate categories
    categories = populate_categories()
    print(f"Total categories: {categories.count()}")
    
    # Populate products
    populate_products(colors, sizes, categories)
    print(f"Total products: {Product.objects.count()}")
    
    print("Database population completed!")

if __name__ == "__main__":
    main()
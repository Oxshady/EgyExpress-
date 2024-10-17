from faker import Faker
import requests
import random
from models.Product import Product
from models.Category import Category
from models.subCategory import Subcategory
from models.Discount import Discount
from models import storage  


faker = Faker()


# Step 1: Populate Categories from Fake Store API
category_map = {}
response = requests.get('https://fakestoreapi.com/products/categories')
api_categories = response.json()

# Create categories in the database
for category_name in api_categories:
    category = Category(
        name=category_name,
        description=faker.sentence()
    )
    category.save()
    category_map[category_name] = category.id  # Save for later use

# Step 2: Generate Subcategories using Faker
subcategory_map = {}
for category_name, category_id in category_map.items():
    subcategories = []
    for _ in range(random.randint(2, 5)):  # Create 2-5 subcategories per category
        subcategory = Subcategory(
            name=faker.word(),
            description=faker.sentence(),
            category_id=category_id
        )
        subcategory.save()  # Save the subcategory to get its ID
        subcategories.append(subcategory.id)
    subcategory_map[category_id] = subcategories

# Step 3: Generate Discounts using Faker
discounts = []
for _ in range(10):  # Create 10 different discounts
    discount = Discount(
        rate=faker.random_int(min=5, max=50)  # Discount between 5% and 50%
    )
    discount.save()  # Save to get the ID
    discounts.append(discount.id)


# Step 4: Populate Products from Fake Store API and link categories
response = requests.get('https://fakestoreapi.com/products')
fake_store_products = response.json()

for product_data in fake_store_products:
    # Find the category ID by comparing product's category with the category map
    category_id = category_map.get(product_data['category'])
    
    # Pick a random subcategory from that category's subcategories
    subcategory_id = random.choice(subcategory_map[category_id])
    
    # Pick a random discount
    discount_id = random.choice(discounts)

    # Create the product
    try:
        product = Product(
            name=product_data['title'],
            image=product_data['image'],
            description="product_data['description']",
            quantity=faker.random_int(min=1, max=100),  # Generate quantity
            price=float(product_data['price']),
            category_id=category_id,
            subcategory_id=subcategory_id,
            discount_id=discount_id
        )
        product.save()
    except Exception as e:
        storage.roll()
        print(e)


# Now you have populated categories, subcategories, discounts, and products!

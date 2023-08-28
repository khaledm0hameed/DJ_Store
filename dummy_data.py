import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
from shop.models import Product



import random
from django.core.files import File  # Import Django's File class
from shop.models import Brand, Product, Category, SubCategory

def seed_Product(n):
    fake = Faker()
    Image = ['car1.jpeg', 'car2.jpeg', 'car3.jpeg', 'car4.jpeg', 'car5.jpeg']
    Flag = ['New', 'Sale', 'Hot', 'feature']

    for _ in range(n):
            product = Product.objects.create(
                Name=fake.name(),
                Price=round(random.uniform(20.99, 99.99),2),
                Description=fake.text(),
                Image = f'images/{Image[random.randint(0,4)]}',
            )
    print(f"Successfully created {n} Products")

seed_Product(100)

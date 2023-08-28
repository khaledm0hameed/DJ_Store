from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.conf import settings
import json
from django.utils import timezone
from account.models import CustomUser
from django.utils.text import slugify
#_________________________________________
class Category(models.Model):
    image = models.ImageField(upload_to='category/',null=True,blank=True)
    name = models.CharField(max_length=50, null=True)
    Slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    def save(self,*args , **kwargs):
        self.Slug = slugify(self.name)
        super(Category,self).save(*args , **kwargs)
#____________________________________________________
class SubCategory(models.Model):
    name= models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    def save(self,*args , **kwargs):
        self.Slug = slugify(self.name)
        super(SubCategory,self).save(*args , **kwargs)
#________________________________________________________
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/',null=True)
    Slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    def save(self,*args , **kwargs):
        self.Slug = slugify(self.name)
        super(Brand,self).save(*args , **kwargs)
#_____________________________________________________
flag = [
    ('New', 'New'),
    ('Sale', 'Sale'),
    ('Hot', 'Hot'),
    ('feature', 'feature')
]

#______________________________________________
class Product(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Product_user',null=True,blank=True)
    Name = models.CharField(max_length=60)
    Price = models.FloatField()
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='images/')
    Availability = models.BooleanField(default=True)
    Color=ColorField(default='#000000')
    Category=models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products",null=True)
    SubCategory=models.ForeignKey(SubCategory, on_delete=models.SET_NULL, related_name="products",null=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="Brand_Product",null=True)
    Flag = models.CharField(choices=flag, max_length=30, null=True, blank=True)
    Slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.Name

    def save(self,*args , **kwargs):
        self.Slug = slugify(self.Name)
        super(Product,self).save(*args , **kwargs)
#________________________________________________________
class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.Name} - {self.quantity_sold} sold"
#______________________________________________________
class Product_Images (models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='Product_images',null=True,blank=True)
    images=models.ImageField(upload_to='productimages/',null=True,blank=True)
#_________________________________________________________

class Review(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,related_name='review_user',null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='review_product',null=True,blank=True)
    content = models.TextField(max_length=20000)
    date = models.DateField(default=timezone.now)
    rate = models.IntegerField(null= True,blank=True)
    def __str__(self):
        return self.content
#__________________________________________________________________________________
class Flash(models.Model):
    pro = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='Flash_product')
    def __str__(self):
        return str(self.pro)
#_____________________________________________________________________________
class Ofer(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='ofer_product',null=True,blank=True)
    def __str__(self):
        return str(self.product)
from django import forms
from shop.models import Product,Review

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Price', 'Description', 'Image', 'Availability', 'Color', 'Category', 'SubCategory', 'Brand', 'Flag']


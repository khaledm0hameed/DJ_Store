from django import forms
from .models import Product,Review

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Price', 'Description', 'Image', 'Availability', 'Color', 'Category', 'SubCategory', 'Brand']



class AddReviewForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=False)
    name = forms.CharField()
    email = forms.EmailField()
    rate = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'class': 'rating-input'}))


from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Brand , Category,SubCategory,Review,Product_Images
from cart.models import Cart,CartItem,Wishlist,wishlistItem
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db import transaction
from django import forms
from django.db.models import Count
from django.views import View
from .forms import AddProductForm,AddReviewForm
from .utils import COLOR_MAP
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.


class ShopGridView(ListView):
    template_name = 'shop/grid.html'
    context_object_name = 'pro'
    paginate_by = 9  # Number of products per page

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', '')
        brand = self.request.GET.get('brand', '')  # Get the brand parameter from the URL
        products = Product.objects.all()

        category_slug = self.kwargs.get('category_id')
        subcategory_slug = self.kwargs.get('sub_id')

        if category_slug:
            products = products.filter(SubCategory__category__Slug=category_slug)

        if subcategory_slug:
            products = products.filter(SubCategory__Slug=subcategory_slug)

        if brand:  # Filter by brand if the brand parameter is provided in the URL
            products = products.filter(Brand__name=brand)

        if sort_by == 'price_high':
            products = products.order_by('-Price')
        elif sort_by == 'price_low':
            products = products.order_by('Price')

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategories = SubCategory.objects.annotate(product_count=Count('products'))
        context['subCategory'] = subcategories

        # Get a list of all available brands and include it in the context
        context['brands'] = Brand.objects.all()

        return context


#___________________________________________________________________________

class ProductDetailView(View):
    template_name = 'shop/detail.html'

    def get_context_data(self, slug):
        pro = Product.objects.get(Slug=slug)
        subcategory = pro.SubCategory
        related = Product.objects.filter(SubCategory=subcategory).exclude(Slug=slug)
        related_images = Product_Images.objects.filter(product=pro)
        color_code = pro.Color
        color_name = COLOR_MAP.get(color_code, 'Unknown Color')
        reviews = Review.objects.filter(product=pro)

        context = {
            'pro': pro,
            'color_name': color_name,
            'reviews': reviews,
            'related': related,
            'related_images': related_images,
        }
        return context

    def get(self, request, slug):
        context = self.get_context_data(slug)
        form = AddReviewForm()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, slug):
        context = self.get_context_data(slug)
        form = AddReviewForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            rate = form.cleaned_data['rate']

            review = Review.objects.create(
                user=request.user,
                product=context['pro'],
                content=content,
                date=timezone.now(),
                rate=rate
            )
            return redirect('detail', slug=slug)
        context['form'] = form
        return render(request, self.template_name, context)
#_______________________________________________________________________________
@login_required
def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/shop')  # Redirect to product list page after adding product
    else:
        form = AddProductForm()

    return render(request, 'shop/add_product.html', {'form': form})




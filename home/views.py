from django.shortcuts import render
from django.db.models import Count
from shop.models import Product, Category,Flash,Ofer,Sales
from cart.models import CartItem, wishlistItem 
from contact.models import Info
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Sum

def product_search_view(request):
    most_sold_products = Product.objects.annotate(total_sales=Sum('sales__quantity_sold')).order_by('-total_sales')[:10]

    info = Info.objects.first()
    cart_items_count = 0
    wishlist_items_count = 0
    flash = Flash.objects.all()
    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(cart__user=request.user).count()
        wishlist_items_count = wishlistItem.objects.filter(wishlist__user=request.user).count()

    search_query = request.GET.get('search_query')
    category_slug = request.GET.get('category', None)  # Change to category_slug
    ofer = Ofer.objects.all()
    products = Product.objects.all()
    pro = Product.objects.order_by('-id')[:4]
    product = Product.objects.all()

    if search_query:
        products = products.filter(Name__icontains=search_query)

    if category_slug:
        products = products.filter(Category__Slug=category_slug)  # Using Category__Slug

    products = products[:4]

    context = {
        'search_query': search_query,
        'products': products,
        'product': product,
        'flash': flash,
        'pro': pro,
        'cart_items_count': cart_items_count,
        'wishlist_items_count': wishlist_items_count,
        'categories': Category.objects.annotate(product_count=Count('products')),
        'ofer': ofer,
        'info': info,
        'most_sold_products': most_sold_products,
    }

    return render(request, 'home/index.html', context)



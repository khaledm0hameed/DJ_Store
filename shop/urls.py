from django.urls import path
from .views import ShopGridView, ProductDetailView, add_product  # Import your views

urlpatterns = [
    path('', ShopGridView.as_view(), name='shop'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('grid/category/<slug:category_id>/', ShopGridView.as_view(), name='grid_by_category'),
    path('grid/category/<slug:category_id>/<slug:sub_id>/', ShopGridView.as_view(), name='grid_by_subcategory'),
    path('add_product/', add_product, name='add_product'),  # Update the view to use the function-based view
]




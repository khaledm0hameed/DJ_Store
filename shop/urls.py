from django.urls import path
from .views import ShopGridView, ProductDetailView  # Import your views

urlpatterns = [
    path('', ShopGridView.as_view(), name='shop'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('grid/category/<slug:category_id>/', ShopGridView.as_view(), name='grid_by_category'),
    path('grid/category/<slug:category_id>/<slug:sub_id>/', ShopGridView.as_view(), name='grid_by_subcategory'),
]




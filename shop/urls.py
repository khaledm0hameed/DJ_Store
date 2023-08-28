from django.urls import path
from .views import ShopView,detail ,  Shop_grid_View , detail
from . import views

urlpatterns = [
    path('', Shop_grid_View, name='shop'),
    path('category/slug:slug>/', views.ShopView, name='shop_by_category'),
    path('list', ShopView, name='grid'),
    path('grid/category/<slug:category_id>/', views.Shop_grid_View, name='grid_by_category'),
    path('grid/category/<slug:category_id>/<slug:sub_id>/', views.Shop_grid_View, name='grid_by_subcategory'),
    path('<slug:slug>',detail,name='detail'),
    path('add_product/',views.add_product,name='add_product')
]
    
    



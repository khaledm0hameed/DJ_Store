from django.contrib import admin
from .models import Product, Category, SubCategory, Brand, Review, Flash, Ofer, Product_Images,Product_Color,Product_Size

# Inline admin class for Product_Images
class ProductImagesTupolar(admin.TabularInline):
    model = Product_Images
class ProductColorTupolar(admin.TabularInline):
    model = Product_Color
# Product admin with inline ProductImagesTupolar

class ProductSizeTupolar(admin.TabularInline):
    model = Product_Size
# Product admin with inline ProductImagesTupolar
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesTupolar,ProductColorTupolar,ProductSizeTupolar]
    search_fields = ['Name']  # Add this line to enable search by product name

# Register models with their respective admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(Flash)
admin.site.register(Ofer)


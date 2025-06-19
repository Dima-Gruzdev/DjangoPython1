from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_product', 'price_to_buy')
    list_filter = ('category_product',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat', )

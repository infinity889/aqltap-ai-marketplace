from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug', 'description', 'available', 'created', 'price']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['price', 'name']
    list_editable = ['price', 'available']



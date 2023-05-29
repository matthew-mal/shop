from django.contrib import admin

from .models import Product, Category


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, AdminCategory)


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image', 'available', 'slug', 'stock']
    list_filter = ['available', 'update', 'date_create']
    list_editable = ['price', 'available', 'stock']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, AdminProduct)

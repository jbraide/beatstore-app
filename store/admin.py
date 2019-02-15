from django.contrib import admin

# Register your models here.
from .models import Genre, Product

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('Name')}

admin.site.register(Genre)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available']
    list_editable = ['price']
    prepopulated_fields = {'slug',('title')}


admin.site.register(Product)

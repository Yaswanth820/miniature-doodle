from django.contrib import admin

from .models import Laptop
# Register your models here.

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rating', 'total_review_count', 'is_refurbished', 'url', 'website')
    search_fields = ('title',)

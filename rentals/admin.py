from django.contrib import admin
from .models import Category , Item , RentalRequest

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')  # نمایش نام و دسته والد در لیست
    list_filter = ('parent',)          # فیلتر بر اساس والد
    search_fields = ('name',)          # جستجو بر اساس نام دسته


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'owner', 'price_per_day', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')


@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display = ('item', 'renter', 'start_date', 'end_date', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('item__name', 'renter__username')
    
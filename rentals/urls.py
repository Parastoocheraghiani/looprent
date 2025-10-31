from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),                          # صفحه اصلی لیست کالاها
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),   # صفحه جزئیات هر کالا
    path('rental-success/<int:rental_id>/', views.rental_success, name='rental_success'),  # صفحه موفقیت ثبت اجاره
]

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Item, Category, Rental
from .forms import RentalRequestForm


def item_list(request):
    category_id = request.GET.get('category')  # گرفتن شناسه دسته از URL
    if category_id:
        items = Item.objects.filter(category_id=category_id)
    else:
        items = Item.objects.all()

    categories = Category.objects.all()
    return render(request, 'rentals/item_list.html', {
        'items': items,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        renter_name = request.POST.get('renter_name')
        renter_phone = request.POST.get('renter_phone')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        message = request.POST.get('message')

        # ✅ ایجاد رکورد جدید در دیتابیس
        rental = Rental.objects.create(
            item=item,
            renter_name=renter_name,
            renter_phone=renter_phone,
            start_date=start_date,
            end_date=end_date,
            message=message,
        )

        # ✅ پیام موفقیت (اختیاری)
        messages.success(request, 'درخواست اجاره شما با موفقیت ثبت شد!')

        # ✅ هدایت به صفحه موفقیت
        return redirect('rental_success', rental_id=rental.id)

    else:
        form = RentalRequestForm()

    return render(request, 'rentals/item_detail.html', {
        'item': item,
        'form': RentalRequestForm()
    })


def rental_success(request, rental_id):
    return render(request, 'rentals/rental_success.html', {'rental_id': rental_id})

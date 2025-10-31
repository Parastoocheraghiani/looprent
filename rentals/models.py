from django.db import models
from django.conf import settings


# ---------------------------
# 🟢 دسته‌بندی کالاها
# ---------------------------
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='دسته والد'
    )

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name


# ---------------------------
# 🟢 کالا
# ---------------------------
class Item(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام کالا")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="دسته")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="مالک")
    price_per_day = models.PositiveIntegerField(verbose_name="قیمت اجاره روزانه (تومان)")
    image = models.ImageField(upload_to='items/', blank=True, null=True, verbose_name="عکس کالا")
    is_available = models.BooleanField(default=True, verbose_name="در دسترس")

    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالاها"

    def __str__(self):
        return self.name


# ---------------------------
# 🟢 رکورد اجاره (Rental)
# ---------------------------
class Rental(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name="کالا")
    renter_name = models.CharField(max_length=100, verbose_name="نام اجاره‌کننده")
    renter_phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    start_date = models.DateField(verbose_name="تاریخ شروع اجاره")
    end_date = models.DateField(verbose_name="تاریخ پایان اجاره")
    message = models.TextField(blank=True, null=True, verbose_name="پیام")  # ✅ اصلاح شد
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "رکورد اجاره"
        verbose_name_plural = "رکوردهای اجاره"

    def __str__(self):
        return f"{self.renter_name} - {self.item.name}"


# ---------------------------
# 🟢 درخواست اجاره (Rental Request)
# ---------------------------
class RentalRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار تأیید'),
        ('accepted', 'تأیید شده'),
        ('rejected', 'رد شده'),
    ]

    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name="کالا")
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="اجاره‌کننده")
    start_date = models.DateField(verbose_name="تاریخ شروع اجاره")
    end_date = models.DateField(verbose_name="تاریخ پایان اجاره")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="وضعیت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده در")

    class Meta:
        verbose_name = "درخواست اجاره"
        verbose_name_plural = "درخواست‌های اجاره"

    def __str__(self):
        return f"{self.item.name} — {self.renter.username} ({self.status})"
    
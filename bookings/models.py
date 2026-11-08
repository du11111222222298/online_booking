from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام خدمت")
    description = models.TextField(verbose_name="توضیحات")
    duration_minutes = models.IntegerField(default=30, verbose_name="مدت زمان (دقیقه)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت (تومان)")

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="خدمت")
    start_time = models.DateTimeField(verbose_name="زمان شروع")
    end_time = models.DateTimeField(verbose_name="زمان پایان")
    is_booked = models.BooleanField(default=False, verbose_name="رزرو شده؟")

    def __str__(self):
        return f"{self.service.name} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    time_slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE, verbose_name="اسلات زمانی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت رزرو")
    status = models.CharField(
        max_length=20, 
        choices=[('Confirmed', 'تایید شده'), ('Cancelled', 'لغو شده')], 
        default='Confirmed',
        verbose_name="وضعیت"
    )

    def __str__(self):
        return f"رزرو {self.user.username} برای {self.time_slot}"
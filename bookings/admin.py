from django.contrib import admin
from .models import Service, TimeSlot, Booking

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_minutes', 'price')

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('service', 'start_time', 'end_time', 'is_booked')
    list_filter = ('is_booked', 'service')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_slot', 'status', 'created_at')
    list_filter = ('status',)

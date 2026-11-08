from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, TimeSlot, Booking

def service_list(request):
    services = Service.objects.all()
    return render(request, 'bookings/service_list.html', {'services': services})

def slot_list(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    # نمایش اسلات‌هایی که هنوز رزرو نشده‌اند
    slots = TimeSlot.objects.filter(service=service, is_booked=False)
    return render(request, 'bookings/slot_list.html', {'service': service, 'slots': slots})

@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(TimeSlot, id=slot_id)
    if not slot.is_booked:
        slot.is_booked = True
        slot.save()
        Booking.objects.create(user=request.user, time_slot=slot)
        return redirect('booking_success')
    return redirect('service_list')

@login_required
def booking_success(request):
    return render(request, 'bookings/success.html')
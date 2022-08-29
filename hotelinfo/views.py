from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from hotelinfo.models import RoomType, IdentityType, Room, Booking, Availability, Customer
from hotelinfo.forms import RoomTypeForm, IdentityTypeForm, RoomForm, CustomerForm, AvailabilityForm, BookingForm
from hotelinfo.utils import PageLinksMixin


class RoomTypeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = RoomType
    permission_required = 'hotelinfo.view_roomtype'


class RoomTypeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = RoomType
    permission_required = 'hotelinfo.view_roomtype'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        room_type = self.get_object()
        room_list = room_type.rooms.all()
        context['room_list'] = room_list
        return context


class RoomTypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RoomTypeForm
    model = RoomType
    permission_required = 'hotelinfo.add_roomtype'


class RoomTypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RoomTypeForm
    model = RoomType
    template_name = 'hotelinfo/roomtype_form_update.html'
    permission_required = 'hotelinfo.change_roomtype'


class RoomTypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = RoomType
    success_url = reverse_lazy('hotelinfo_room_type_list_urlpattern')
    permission_required = 'hotelinfo.delete_roomtype'

    def get(self, request, pk):
        roomtype = get_object_or_404(RoomType, pk=pk)
        rooms = roomtype.rooms.all()
        if rooms.count() > 0:
            return render(
                request,
                'hotelinfo/roomtype_refuse_delete.html',
                {'roomtype': roomtype,
                 'rooms': rooms,
                 }
            )
        else:
            return render(
                request,
                'hotelinfo/roomtype_confirm_delete.html',
                {'roomtype': roomtype}
            )


class IdentityTypeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = IdentityType
    permission_required = 'hotelinfo.view_identitytype'


class IdentityTypeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = IdentityType
    permission_required = 'hotelinfo.view_identitytype'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        identity_type = self.get_object()
        customer_list = identity_type.customers.all()
        context['customer_list'] = customer_list
        return context


class IdentityTypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = IdentityTypeForm
    model = IdentityType
    permission_required = 'hotelinfo.add_identitytype'


class IdentityTypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = IdentityTypeForm
    model = IdentityType
    template_name = 'hotelinfo/identitytype_form_update.html'
    permission_required = 'hotelinfo.change_identitytype'


class IdentityTypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = IdentityType
    success_url = reverse_lazy('hotelinfo_identity_type_list_urlpattern')
    permission_required = 'hotelinfo.delete_identitytype'

    def get(self, request, pk):
        identitytype = get_object_or_404(IdentityType, pk=pk)
        customers = identitytype.customers.all()
        if customers.count() > 0:
            return render(
                request,
                'hotelinfo/identitytype_refuse_delete.html',
                {'identitytype': identitytype,
                 'customers': customers,
                 }
            )
        else:
            return render(
                request,
                'hotelinfo/identitytype_confirm_delete.html',
                {'identitytype': identitytype}
            )


class RoomList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Room
    permission_required = 'hotelinfo.view_room'


class RoomDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Room
    permission_required = 'hotelinfo.view_room'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        room = self.get_object()
        room_type = room.room_type
        availability_list = room.availabilitys.all()
        context['room_type'] = room_type
        context['availability_list'] = availability_list
        return context


class RoomCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RoomForm
    model = Room
    permission_required = 'hotelinfo.add_room'


class RoomUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RoomForm
    model = Room
    template_name = 'hotelinfo/room_form_update.html'
    permission_required = 'hotelinfo.change_room'


class RoomDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Room
    success_url = reverse_lazy('hotelinfo_room_list_urlpattern')
    permission_required = 'hotelinfo.delete_room'

    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        availabilitys = room.availabilitys.all()
        if availabilitys.count() > 0:
            return render(
                request,
                'hotelinfo/room_refuse_delete.html',
                {'room': room,
                 'availabilities': availabilitys,
                 }
            )
        else:
            return render(
                request,
                'hotelinfo/room_confirm_delete.html',
                {'room': room}
            )


class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Customer
    permission_required = 'hotelinfo.view_customer'


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    permission_required = 'hotelinfo.view_customer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        customer = self.get_object()
        identity_type = customer.id_type
        booking_list = customer.bookings.all()
        context['identity_type'] = identity_type
        context['booking_list'] = booking_list
        return context


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CustomerForm
    model = Customer
    permission_required = 'hotelinfo.add_customer'


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'hotelinfo/customer_form_update.html'
    permission_required = 'hotelinfo.change_customer'


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('hotelinfo_customer_list_urlpattern')
    permission_required = 'hotelinfo.delete_customer'

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        bookings = customer.bookings.all()
        if bookings.count() > 0:
            return render(
                request,
                'hotelinfo/customer_refuse_delete.html',
                {'customer': customer,
                 'bookings': bookings,
                 }
            )
        else:
            return render(
                request,
                'hotelinfo/customer_confirm_delete.html',
                {'customer': customer}
            )


class AvailabilityList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Availability
    permission_required = 'hotelinfo.view_availability'


class AvailabilityDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Availability
    permission_required = 'hotelinfo.view_availability'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        availability = self.get_object()
        room = availability.room
        booking_list = availability.bookings.all()
        context['room'] = room
        context['booking_list'] = booking_list
        return context


class AvailabilityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AvailabilityForm
    model = Availability
    permission_required = 'hotelinfo.add_availability'


class AvailabilityUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AvailabilityForm
    model = Availability
    template_name = 'hotelinfo/availability_form_update.html'
    permission_required = 'hotelinfo.change_availability'


class AvailabilityDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Availability
    success_url = reverse_lazy('hotelinfo_availability_list_urlpattern')
    permission_required = 'hotelinfo.delete_availability'

    def get(self, request, pk):
        availability = get_object_or_404(Availability, pk=pk)
        bookings = availability.bookings.all()
        if bookings.count() > 0:
            return render(
                request,
                'hotelinfo/availability_refuse_delete.html',
                {'availability': availability,
                 'bookings': bookings,
                 }
            )
        else:
            return render(
                request,
                'hotelinfo/availability_confirm_delete.html',
                {'availability': availability}
            )


class BookingList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Booking
    permission_required = 'hotelinfo.view_booking'


class BookingDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Booking
    permission_required = 'hotelinfo.view_booking'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        booking = self.get_object()
        customer = booking.customer
        room_availability = booking.room_availability
        context['customer'] = customer
        context['room_availability'] = room_availability
        return context


class BookingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = BookingForm
    model = Booking
    permission_required = 'hotelinfo.add_booking'


class BookingUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = BookingForm
    model = Booking
    template_name = 'hotelinfo/booking_form_update.html'
    permission_required = 'hotelinfo.change_booking'


class BookingDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('hotelinfo_booking_list_urlpattern')
    permission_required = 'hotelinfo.delete_booking'

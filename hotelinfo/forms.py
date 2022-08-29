from django import forms
from hotelinfo.models import RoomType, IdentityType, Room, Customer, Availability, Booking


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'

        def clean_room_type(self):
            return self.cleaned_data['room_type'].strip()

        def clean_room_area(self):
            return self.cleaned_data['room_area'].strip()


class IdentityTypeForm(forms.ModelForm):
    class Meta:
        model = IdentityType
        fields = '__all__'

        def clean_identity_type(self):
            return self.cleaned_data['identity_type'].strip()


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

        def clean_room_number(self):
            return self.cleaned_data['room_number'].strip()

        def clean_floor_number(self):
            return self.cleaned_data['floor_number'].strip()


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        def clean_first_name(self):
            return self.cleaned_data['first_name'].strip()

        def clean_last_name(self):
            return self.cleaned_data['last_name'].strip()

        def clean_id_number(self):
            return self.cleaned_data['id_number'].strip()


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'

        def clean_check_in(self):
            return self.cleaned_data['check_in'].strip()

        def clean_check_out(self):
            return self.cleaned_data['check_out'].strip()


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

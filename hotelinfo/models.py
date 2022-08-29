from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class RoomType(models.Model):
    roomType_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=45, unique=True)
    room_area = models.IntegerField(default=10)

    def __str__(self):
        return '%s' % self.room_type

    def get_absolute_url(self):
        return reverse('hotelinfo_room_type_detail_urlpattern', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('hotelinfo_room_type_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('hotelinfo_room_type_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['room_type']


class IdentityType(models.Model):
    identity_id = models.AutoField(primary_key=True)
    identity_type = models.CharField(max_length=45, unique=True)
    government_issued_id = models.BooleanField()

    def __str__(self):
        return '%s' % self.identity_type

    def get_absolute_url(self):
        return reverse('hotelinfo_identity_type_detail_urlpattern', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('hotelinfo_identity_type_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('hotelinfo_identity_type_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['identity_type']


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    room_type = models.ForeignKey(RoomType, related_name='rooms', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.room_number, self.room_type.room_type)

    def get_absolute_url(self):
        return reverse('hotelinfo_room_detail_urlpattern', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('hotelinfo_room_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('hotelinfo_room_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['room_number']
        constraints = [UniqueConstraint(fields=['room_number', 'floor_number'], name='unique_room')]


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    id_type = models.ForeignKey(IdentityType, related_name='customers', on_delete=models.PROTECT)
    id_number = models.CharField(max_length=45)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('hotelinfo_customer_detail_urlpattern', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('hotelinfo_customer_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('hotelinfo_customer_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'id_type', 'id_type']
        constraints = [UniqueConstraint(fields=['last_name', 'first_name', 'id_type', 'id_type'], name='unique_customer')]


class Availability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, related_name='availabilitys', on_delete=models.PROTECT)

    def __str__(self):
        return 'Room %s - %s - %s' % (self.room.room_number, self.check_in, self.check_out)

    def get_absolute_url(self):
        return reverse('hotelinfo_availability_detail_urlpattern', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('hotelinfo_availability_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('hotelinfo_availability_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['room__room_number', 'check_in', 'check_out']
        constraints = [UniqueConstraint(fields=['room', 'check_in', 'check_out'], name='unique_availability')]


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='bookings', on_delete=models.PROTECT)
    room_availability = models.ForeignKey(Availability, related_name='bookings', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.customer, self.room_availability)

    def get_absolute_url(self):
        return reverse('hotelinfo_booking_detail_urlpattern', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('hotelinfo_booking_update_urlpattern', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('hotelinfo_booking_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['customer__last_name', 'room_availability__room__room_number']
        constraints = [UniqueConstraint(fields=['customer', 'room_availability'], name='unique_booking')]

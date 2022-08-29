from django.contrib import admin
from.models import Room, RoomType, Booking, Availability, Customer, IdentityType

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Customer)
admin.site.register(Availability)
admin.site.register(Booking)
admin.site.register(IdentityType)

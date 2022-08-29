from django.urls import path

from hotelinfo.views import (
    RoomTypeList, RoomTypeDetail, IdentityTypeList, IdentityTypeDetail, RoomList, RoomDetail,
    CustomerList, CustomerDetail, AvailabilityList, AvailabilityDetail, BookingList, BookingDetail,
    RoomTypeCreate, IdentityTypeCreate, RoomCreate, CustomerCreate, AvailabilityCreate, BookingCreate,
    RoomTypeUpdate, IdentityTypeUpdate, RoomUpdate, CustomerUpdate, AvailabilityUpdate, BookingUpdate,
    RoomTypeDelete, IdentityTypeDelete, RoomDelete, CustomerDelete, AvailabilityDelete, BookingDelete
)

urlpatterns = [
    path('roomtype/',
         RoomTypeList.as_view(),
         name='hotelinfo_room_type_list_urlpattern'),
    path('roomtype/<int:pk>/',
         RoomTypeDetail.as_view(),
         name='hotelinfo_room_type_detail_urlpattern'),
    path('roomtype/create/',
         RoomTypeCreate.as_view(),
         name='hotelinfo_room_type_create_urlpattern'),
    path('roomtype/<int:pk>/update/',
         RoomTypeUpdate.as_view(),
         name='hotelinfo_room_type_update_urlpattern'),
    path('roomtype/<int:pk>/delete/',
         RoomTypeDelete.as_view(),
         name='hotelinfo_room_type_delete_urlpattern'),

    path('identitytype/',
         IdentityTypeList.as_view(),
         name='hotelinfo_identity_type_list_urlpattern'),
    path('identitytype/<int:pk>/',
         IdentityTypeDetail.as_view(),
         name='hotelinfo_identity_type_detail_urlpattern'),
    path('identitytype/create/',
         IdentityTypeCreate.as_view(),
         name='hotelinfo_identity_type_create_urlpattern'),
    path('identitytype/<int:pk>/update/',
         IdentityTypeUpdate.as_view(),
         name='hotelinfo_identity_type_update_urlpattern'),
    path('identitytype/<int:pk>/delete/',
         IdentityTypeDelete.as_view(),
         name='hotelinfo_identity_type_delete_urlpattern'),

    path('room/',
         RoomList.as_view(),
         name='hotelinfo_room_list_urlpattern'),
    path('room/<int:pk>/',
         RoomDetail.as_view(),
         name='hotelinfo_room_detail_urlpattern'),
    path('room/create/',
         RoomCreate.as_view(),
         name='hotelinfo_room_create_urlpattern'),
    path('room/<int:pk>/update/',
         RoomUpdate.as_view(),
         name='hotelinfo_room_update_urlpattern'),
    path('room/<int:pk>/delete/',
         RoomDelete.as_view(),
         name='hotelinfo_room_delete_urlpattern'),

    path('customer/',
         CustomerList.as_view(),
         name='hotelinfo_customer_list_urlpattern'),
    path('customer/<int:pk>/',
         CustomerDetail.as_view(),
         name='hotelinfo_customer_detail_urlpattern'),
    path('customer/create/',
         CustomerCreate.as_view(),
         name='hotelinfo_customer_create_urlpattern'),
    path('customer/<int:pk>/update/',
         CustomerUpdate.as_view(),
         name='hotelinfo_customer_update_urlpattern'),
    path('customer/<int:pk>/delete/',
         CustomerDelete.as_view(),
         name='hotelinfo_customer_delete_urlpattern'),

    path('availability/',
         AvailabilityList.as_view(),
         name='hotelinfo_availability_list_urlpattern'),
    path('availability/<int:pk>/',
         AvailabilityDetail.as_view(),
         name='hotelinfo_availability_detail_urlpattern'),
    path('availability/create/',
         AvailabilityCreate.as_view(),
         name='hotelinfo_availability_create_urlpattern'),
    path('availability/<int:pk>/update/',
         AvailabilityUpdate.as_view(),
         name='hotelinfo_availability_update_urlpattern'),
    path('availability/<int:pk>/delete/',
         AvailabilityDelete.as_view(),
         name='hotelinfo_availability_delete_urlpattern'),

    path('booking/',
         BookingList.as_view(),
         name='hotelinfo_booking_list_urlpattern'),
    path('booking/<int:pk>/',
         BookingDetail.as_view(),
         name='hotelinfo_booking_detail_urlpattern'),
    path('booking/create/',
         BookingCreate.as_view(),
         name='hotelinfo_booking_create_urlpattern'),
    path('booking/<int:pk>/update/',
         BookingUpdate.as_view(),
         name='hotelinfo_booking_update_urlpattern'),
    path('booking/<int:pk>/delete/',
         BookingDelete.as_view(),
         name='hotelinfo_booking_delete_urlpattern'),

]
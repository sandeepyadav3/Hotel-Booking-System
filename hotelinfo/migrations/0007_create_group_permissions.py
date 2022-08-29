from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    room_type_permissions = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                            content_type__model='roomtype')

    identity_type_permissions = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                                content_type__model='identitytype')

    room_permissions = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                       content_type__model='room')

    customer_permissions = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                           content_type__model='customer')

    availability_permissions = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                               content_type__model='availability')

    booking_permissions = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                          content_type__model='booking')

    perm_view_room_type = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                          content_type__model='roomtype',
                                                          codename='view_roomtype')

    perm_view_identity_type = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                              content_type__model='identitytype',
                                                              codename='view_identitytype')

    perm_view_room = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                     content_type__model='room',
                                                     codename='view_room')

    perm_view_customer = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                         content_type__model='customer',
                                                         codename='view_customer')

    perm_view_availability = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                             content_type__model='availability',
                                                             codename='view_availability')

    perm_view_booking = permission_class.objects.filter(content_type__app_label='hotelinfo',
                                                        content_type__model='booking',
                                                        codename='view_booking')

    hi_user_permissions = chain(perm_view_room_type,
                                perm_view_identity_type,
                                perm_view_room,
                                perm_view_customer,
                                perm_view_availability,
                                perm_view_booking)

    hi_manager_permissions = chain(customer_permissions,
                                   availability_permissions,
                                   booking_permissions,
                                   perm_view_room_type,
                                   perm_view_identity_type,
                                   perm_view_room)

    hi_admin_permissions = chain(room_type_permissions,
                                 identity_type_permissions,
                                 room_permissions,
                                 perm_view_customer,
                                 perm_view_availability,
                                 perm_view_booking)

    my_groups_initialization_list = [
        {
            "name": "hi_user",
            "permissions_list": hi_user_permissions,
        },
        {
            "name": "hi_manager",
            "permissions_list": hi_manager_permissions,
        },
        {
            "name": "hi_admin",
            "permissions_list": hi_admin_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('hotelinfo', '0006_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]

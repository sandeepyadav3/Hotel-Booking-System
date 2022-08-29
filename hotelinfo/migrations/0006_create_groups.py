from django.db import migrations

GROUPS = [
    {
        'name': 'hi_user',
    },
    {
        'name': 'hi_manager',
    },
    {
        'name': 'hi_admin',
    },
]


def add_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.create(
            name=group['name'],
        )


def remove_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.get(
            name=group['name']
        )
        group_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('hotelinfo', '0005_roomtype_room_area'),
    ]

    operations = [

        migrations.RunPython(
            add_group_data,
            remove_group_data
        )

    ]
